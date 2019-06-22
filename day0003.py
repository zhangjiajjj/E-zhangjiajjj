import requests
url='http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808'
response=requests.get(url)
HTML=response.text
URLS=HTML.split_('"')
# if '<jpg' in HTML:
#         split_=line.split('<jpg src=')
if '<jpg' in url:
    URLS.append(url)
for url in URLS:
    response=requests.get(url)
    content=response.content
    name=url.split('/')[-1]

with open(response.text,'wb') as f:
    f.write(content)

