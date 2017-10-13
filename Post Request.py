import requests

headers = {
    'X-Events-API-AccountName' : 'customer1_93f127e2-b947-4318-b3c0-260567c8cfca',
    'X-Events-API-Key' : 'bf4ab826-cd49-499b-82d5-969717bc16ba',
    'Content-type' : 'application/vnd.appd.events+text;v=1'
}

data = '[{"First": "asdfasdf","Second": "ACME"}]'

requests.post('54.213.100.234:9080/events/publish/raxog', headers=headers, data=data)