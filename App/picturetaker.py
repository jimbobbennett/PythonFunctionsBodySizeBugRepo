import requests

functionUrl = "http://localhost:7071/api/UploadPhoto"

data = open('./photo.jpg', 'rb').read()
print('Data length:', len(data))
res = requests.post(url=functionUrl,
                    data=data,
                    headers={'Content-Type': 'application/octet-stream'})
