import requests
res=requests.get('http://www.baidu.com')
with open('zz.txt',mode='w',encoding='utf8') as f:
    f.write(res.text)

urls={'http://www.baidu.com/s?wd=zz'}
url='http://www.baidu.com/s?'
res1=requests.get(url,params={'wd':'狗'})
res2=requests.get(url,params={'wd':'郝锦荣'})
res3=requests.get(url,params={'wd':'王欣欣'})
print(res1.url,res2.url,res3.url)
with open('zz.txt',mode='w',encoding='utf8') as f:
    f.write(res1.text)
    f.write(res2.text)
    f.write(res3.text)
HTML=response.text
lines=HTML.split('\n')
    if 'http' in res1.text or 'https' in res1.text:
        url=i.split('"')[1]
response=requests.get(url)
content=response.content
name=url.split('/')[-1]
with open(name,'wb') as f:
    f.write(content)