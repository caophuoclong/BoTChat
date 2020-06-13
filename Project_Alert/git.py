from webhooks import webhook
from webhooks.senders import targeted

@webhook(sender_callable=targeted.sender)
def basic(url, wife, husband):
    return {"husband": husband, "wife": wife}

r = basic(url="http://httpbin.org/post", husband="Danny", wife="Audrey")
import pprint
pprint.pprint(r)
{'attempt': 1,
'hash': '29788eb987104b8a87d201292fa459d9',
'husband': 'Danny',
'response': b'{\n  "args": {},\n  "data": "",\n  "files": {},\n  "form": {\n    "attempt": "1",\n    "hash": "29788eb987104b8a87d201292fa459d9",\n    "husband": "Danny",\n    "url": "http://httpbin.org/post",\n    "wife": "Audrey"\n  },\n  "headers": {\n    "Accept": "*/*",\n    "Accept-Encoding": "gzip, deflate",\n    "Connection": "close",\n    "Content-Length": "109",\n    "Content-Type": "application/x-www-form-urlencoded",\n    "Host": "httpbin.org",\n    "User-Agent": "python-requests/2.3.0 CPython/3.3.5 Darwin/12.3.0",\n    "X-Request-Id": "d25119e4-08ba-4523-abc4-b9a9ac10225b"\n  },\n  "json": null,\n  "origin": "108.185.146.101",\n  "url": "http://httpbin.org/post"\n}',
'status_code': 200,
'url': 'http://httpbin.org/post',
'wife': 'Audrey'}