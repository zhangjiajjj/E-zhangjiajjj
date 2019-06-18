import urllib.request
import urllib.parse
data = urllib.parse.urlencode({'wd':'嘿嘿'})
print(data)
url = 'http://www.baidu.com/s?' + data
response = urllib.request.urlopen(url)
HTML = response.read().decode('utf8')
print(HTML)
data = bytes(urllib.parse.urlencode({'pw':'123','456':'789'}),enconding='utf8')
url = 'http://httpbin.org/post'
response = urllib.request.urlopen(url,data=data)
result = response.read().decode('utf8')
print(result)