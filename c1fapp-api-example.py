import json
import sys
import os
import argparse
import sys

try:
    import requests
except:
    print "Please install requests (pip install requests)."
    sys.exit(-1)
try:
    from jinja2 import Environment, FileSystemLoader
except:
    print "Please install Jinja2 (pip install jinja2)."
    sys.exit(-1)
try:
    from prettytable import PrettyTable
except:
    print "Please install prettytable (pip install prettytable)."
    sys.exit(-1)

API_URL = "https://www.c1fapp.com/cifapp/api/"
API_KEY = ""

parser = argparse.ArgumentParser(prog="c1fapp-api-example.py",
                                 description='C1fApp API Threat Search')
parser.add_argument("-s", action="store", dest='search',
                    help="Search ip/domain/url", required=True)
parser.add_argument("-f", action="store", dest='file',
                    help="file name is required")
parser.add_argument("-v", action="version",
                    version="%(prog)s 1.0")
args = parser.parse_args()

if args.search is None:
    parser.parse_args(['-h'])

c1fappTab = PrettyTable(["feed label",
                             "domain",
                             "description",
                             "assessment",
                             "confidence",
                             "reportime",
                             "ipaddress",
                             "asn"
    ])

session = requests.Session()

payload = {'key': API_KEY,
           'format': 'json',
           'backend': 'es',
           'request': args.search
}

c1fapp_query = session.post(API_URL, data=json.dumps(payload))

try:
    results = json.loads(c1fapp_query.text)
except ValueError:
    print "No JSON object could be decoded."
    sys.exit(-1)

r = []
if len(results) > 0:
    for res in results:
        confidence = str(res['confidence'][0])
        asn = str(res['asn'][0])
        res['confidence'] = confidence

        c1fappTab.add_row([''.join(res['feed_label']),
                               ''.join(res['domain']),
                               ''.join(res['description']),
                               ''.join(res['assessment']),
                               ''.join(confidence),
                               ''.join(res['reportime']),
                               ''.join(res['ip_address']),
                               ''.join(asn)
            ])
        r.append(res)

else:
    print "No data found for the search {}.".format(args.search)
    sys.exit(-1)

print "Number of results found <{}>.".format(len(results))
print c1fappTab

if args.file:
    if not os.path.exists("export"):
        os.makedirs("export")

    exportpath = "export/{}".format(args.file)
    fo = open(exportpath, "w")
    env = Environment(loader=FileSystemLoader("./"), trim_blocks=True)
    mytemplate = env.get_template('c1fappres.html').render(c1fappres=r,
                                                           domain_name=args.search,
                                                           number=len(results))
    fo.write(mytemplate.encode('utf-8'))
    fo.close
