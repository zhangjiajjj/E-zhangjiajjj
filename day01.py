print('hello world')

def function(num):
    return num *10

if __name__=="__main__":
    print(function(10))

import requests
#请求百度，需要注意：一定带上http/https
response= requests.get('http://www.baidu.com')
print(response)
print(response.text)
print(response.headers)
headers=User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0
print()



from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')