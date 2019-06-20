#爬取http://www.17k.com/chapter/2933095/36699279.html存入本地
import urllib.request
url = 'http://www.17k.com/chapter/2933095/36699279.html'
#创建request
request=urllib.request.Request(url)
#发送请求获取结果
response = urllib.request.urlopen(request)
data = response.read()
data = data.decode('utf-8')
#打印结果
print (data)
#爬取数据保存到文件
file = open(url,encoding='utf-8')
file.write(htmldata)
file.close()


#自己仿照多建几个代理
#访问一个网站，如果状态码不是200
#尝试更换代理继续访问
#
import urllib,request
import random
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
url = 'http://baidu.com'
proxy_handle = [{'http://1.198.73.189:9999'},{'http://111.226.211.11:8118'},{'http://175.181.40.199:44308'}]
while 1:
    print(proxy_handle.pop())
    print(proxy_handle)
    if len(proxy_handle) ==0:
        print('爬取失败')
proxy = urllib.request.ProxyHandler(proxy_handle)
opener = urllib.request.build_opener(proxy_handle)
reponse = opener.open(url)
print(reponse.read())

