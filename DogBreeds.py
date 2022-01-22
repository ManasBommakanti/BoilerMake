import http.client

conn = http.client.HTTPSConnection("api.thedogapi.com")

headers = { 'x-api-key': "9207caa6-f2dc-4493-8d61-5cf3ad0e3c3f" }

conn.request("GET", "/v1/breeds?attach_breed=0", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))