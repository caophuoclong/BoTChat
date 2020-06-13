import http.client

conn = http.client.HTTPSConnection('48688f2f8529a2d2fd2630be335733d6.m.pipedream.net')
conn.request("POST", '/', '{"message":"The force is strong with this one..."}', {
  'Content-Type': 'application/json',
})

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))