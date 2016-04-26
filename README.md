## Lookup API for C1fApp threat feed service


### How can I query C1fApp for an address ?

When you query the C1fApp API you will not receive dymanic results, but only static ones. The difference is that no external resources are queried but only the internal C1fApp repository with historic data. The dynamic checks are only available via the C1fApp Dashboard.

We provide historic searches and the API is looking up to three months in the past from the time of query. So if an IPv4 address for example appeared in a feed two months ago, the search will still return this result. To make it easier for the end user or device to evaluate the result we suggest to look at the last time this entry appeared in the feeds. 


### Use the API interface
REST API with JSON

```
curl -X POST -i -d '{"key":"API_KEY","format":"json","backend":"es","request":"HOST_QUERY"}' https://www.c1fapp.com/cifapp/api/ --header "Content-Type:application/json"

```
Parameters

* Format: json
* Backend: es
* key: Your API key
* HOST_QUERY: IPv4 or Domain

Response


```
[
    {
        "feed_label": [
            "Abuse.ch"
        ], 
        "domain": [
            "barselkab.bps.go.id"
        ], 
        "description": [
            "Zeus botnet"
        ], 
        "derived": "direct", 
        "address": [
            "barselkab.bps.go.id"
        ], 
        "ip_address": [
            "203.123.60.144"
        ], 
        "asn": [
            "38755"
        ], 
        "confidence": [
            "70"
        ], 
        "country": [
            "ID"
        ], 
        "reportime": [
            "2016-02-03"
        ], 
        "source": [
            "https://zeustracker.abuse.ch/monitor.php", 
            "https://zeustracker.abuse.ch/monitor.php"
        ], 
        "asn_desc": [
            "Biro Statistics"
        ], 
        "assessment": [
            "botnet"
        ]
    }, 
    {
        "feed_label": [
            "Abuse.ch"
        ], 
        "domain": [
            "barselkab.bps.go.id"
        ], 
        "description": [
            "Zeus botnet"
        ], 
        "derived": "direct", 
        "address": [
            "barselkab.bps.go.id"
        ], 
        "ip_address": [
            "203.123.60.144"
        ], 
        "asn": [
            "38755"
        ], 
        "confidence": [
            "70"
        ], 
        "country": [
            "ID"
        ], 
        "reportime": [
            "2016-02-04"
        ], 
        "source": [
            "https://zeustracker.abuse.ch/monitor.php", 
            "https://zeustracker.abuse.ch/monitor.php"
        ], 
        "asn_desc": [
            "Biro Statistics"
        ], 
        "assessment": [
            "botnet"
        ]
    }
]

```

### What are the restrictions for API key usage?

Depending on the subscription you have, the below (hard limit) restrictions apply on the API usage


| First Header  | Second Header |
| ------------- | ------------- |
| Light  | 50 API requests/day  |
| Premium  | 3K API requests/day  |
| OEM  | 100K requests/day  |





