# 爬虫基本逻辑使用

使用程序模拟浏览器，去向服务器发送请求，获取有用数据信息！



## 爬虫的核心

```
爬取网页：爬取整个网页、包含子网页中所有的信息
解析数据：将网页中得到的数据进行解析
难点：爬虫和反爬虫之间的博弈
```





## 爬取网页

### requests基本使用

**安装requests**

```
进入到python文件目录下
pip install requests
```

###  

**文档说明：**

[官方文档](https://docs.python-requests.org/zh_CN/latest/)、[快速上手](https://docs.python-requests.org/zh_CN/latest/user/quickstart.html)



**基本语法**

| 类型          | 功能                  |
| ------------- | --------------------- |
| r.get         | get —模拟浏览器访问   |
| r.post        | post — 模拟浏览器访问 |
| r.text        | 获取网站源码          |
| r.encoding    | 访问或定制编码方式    |
| r.url         | 获取请求的url         |
| r.content     | 响应的字节类型        |
| r.status_code | 响应的状态码          |
| r.headers     | 响应的头信息          |



### get请求

![image-20220405084630898](/Users/Zander/Typora库/img/image-20220405084630898.png)

![image-20220405082416605](/Users/Zander/Typora库/img/image-20220405082416605-9118267.png)

```python
# 导入requests
import requests


# 获取请求地址
url_1 = 'https://www.baidu.com/s?wd=%周杰伦' # 完整的请求地址

url_2 = 'https://www.baidu.com/s?' # 缺少参数的请求地址,具体看实际需求
data = {'wd':'周杰伦'}


# 获取请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
}


# 模拟浏览器访问
response = requests.get(url=url,params=data,headers=headers) # 如果没有data可以不传入params
```



### post请求

![image-20220405084420713](/Users/Zander/Typora库/img/image-20220405084420713-9119463-9119466.png)

```python
# eg:百度翻译

# 导入requests
import requests


# 获取请求地址
url = 'https://fanyi.baidu.com/sug'
data = {'kw':'love'} -- 传递的参与，love可以是其他变量单词


# 获取请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
}


# 模拟浏览器访问
response = requests.post(url=url,data=data,headers=headers) 
```



###  get请求和post请求的区别

| 请求方式 | 编码         | 参数                 | encode调用       |
| -------- | ------------ | -------------------- | ---------------- |
| get      | 参数必须编码 | 拼接到url之后        | 不需要encode调用 |
| psot     | 参数必须编码 | 参数是放在对象定制中 | 需要encode调用   |



### cookie定制

cookie会记住我们的数据信息，然后当特定用户登入会进行数据交换，如果涉及到登陆的爬虫则需要用到cookie定制

cookie请求一般请求数据会带在post请求里面，所以原理和post请求一样，一般我们登陆时候故意输错密码，然后数据文件中一般会有一个名为logxxxxx的文件里面携带表单数据

![image-20220405090337668](/Users/Zander/Typora库/img/image-20220405090337668.png)

```python
data={
  	'__VIEWSTATE':'La4Z9fymCBZt4ZHrRdLLDWklr0MKTC4cScOjB1ZCb5bMUsj1YhjXSC16yT0d0WCEjcUSZ/NHtSeFEB9KRT5hF1XoJ/RW1m0/GGAvsdAaSY5MNWgmSgMmC8eWWKc='
    '__VIEWSTATEGENERATOR': 'C93BE1AE'
    'from': 'http://so.gushiwen.cn/user/collect.aspx'
    'email': '15389552031'
     'pwd': 'sdasdasdsa'
    'code': 'xoat'
    'denglu': '登录'
}
# 然后将data传入requests.post()中


# 其中email\pwd是我们自己输入的账号密码，denglu 是登陆 -- 都是固定的
# '__VIEWSTATE'和'__VIEWSTATEGENERATOR'是变动的需要在每次登陆页面的源码中获取 -- xpath
# code 也是在每次登陆中获取 -- 可以通过超级鹰自动验证码识别
```



### 验证码识别

超级鹰



### 代理

可以在请求中设置proxies参数传入代理IP即可，参数类型是一个字典类型

```python
# 导入随机库
import random


# 设置代理池 -- 池中的单个代理也是字典类型
proxies_s = {
    {'http':'219.149.59.250:9797'},
    {'http':'219.149.59.250:9797'},
    {'http':'219.149.59.250:9797'},
    {'http':'219.149.59.250:9797'},
}


# 随机获取一个代理
proxies = random.choice(proxoes_s)
```





## 解析数据

### HTML解析 — Xpath



#### Xpath安装

**Xpath插件安装**

```
浏览器插件搜索XPath Helper
安装到扩展程序中
重启浏览器
调用方法：ctrl+shift+X -- 出现小黑框就可以使用了
```

**lxml库安装**

```python
pip install lxml 

pip install lxml ‐i https://pypi.douban.com/simple # 国内源
```



#### 调用解析

```python
# 导入lxml.etree
from lxml import etree


# 解析本地文件
tree = etree.parse('xx.html')


# 解析服务器响应文件
tree = etree.HTML('xx.html')


# xpath查询
tree.xpath('xpath路径')
```



#### 节点定位

**演示案例**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"/>
    <title>Title</title>
</head>
<body>
    <ul>
        <li id="l1" class="c1">北京</li>
        <li id="l2">上海</li>
        <li id="c3">深圳</li>
        <li id="c4">武汉</li>
    </ul>

    <li>山东</li>
    <li id="5c">辽宁</li>
    <li>西安</li>

</body>
</html>
```

| 语法                         | 功能                               | 实例                                     | 结果                               |
| ---------------------------- | ---------------------------------- | ---------------------------------------- | ---------------------------------- |
| //                           | 查找所有的子孙节点，不考虑层级关系 | tree.xpath('//body//li')                 | 返回七个li标签                     |
| /                            | 查找直接子节点                     | tree.xpath('//body/ul/li')               | 返回北京、上海、深圳、武汉的li标签 |
| //div[@属性]                 | 查询包含某个属性的节点             | tree.xpath('//li[@id]')                  | 返回北京、上海、深圳、武汉的li标签 |
| //div[@属性=“xxxxxx”]        | 查询符合这个属性值的节点           | tree.xpath('//li[@class="c1"]')          | 返回北京的li标签                   |
| //div[contains(@属性,”xx”)]  | 查询属性值中包含xx的节点           | Tree.xpath(''//li[contains(@id,"c")]')   | 返回深圳、武汉、辽宁所在标签       |
| //div[starts-with(@id,”xx”)] | 查询属性值中以xx开头的节点         | tree.xpath('//li[starts-with(@id,"c")]') | 返回深圳、武汉所在标签             |



#### 节点信息

演示案例同节点定位

| 语法    | 功能               | 实例                              | 结果                             |
| ------- | ------------------ | --------------------------------- | -------------------------------- |
| /text() | 获取文本内容       | tree.xpath('//body/ul/li/text()') | ['北京', '上海', '深圳', '武汉'] |
| /@属性  | 获取属性所对应的值 | tree.xpath('//body/ul/li/@id')    | ['l1', 'l2', 'c3', 'c4']         |





### JSON解析 — JsonPath

[教程说明](http://blog.csdn.net/luxideyao/article/details/77802389)



#### JsonPath安装

```
pip install jsonpath
```



#### 调用解析

```python
# 导入json库
import json
import jsonpath


# 获取json文件 -- 只可以解析本地文件
obj = json.load(open('路径.json','r',encodeing='utf-8'))


# json节点查询
ret = jsonpath.jsonpath(obj,'jsonpath语法')
```



#### jsonpath解析语法

**演示案例**

```json
{ "store": {
    "book": [
      { "category": "修真",
        "author": "六道",
        "title": "坏蛋是怎样练成的",
        "price": 8.95
      },
      { "category": "修真",
        "author": "天蚕土豆",
        "title": "斗破苍穹",
        "price": 12.99
      },
      { "category": "修真",
        "author": "唐家三少",
        "title": "斗罗大陆",
        "isbn": "0-553-21311-3",
        "price": 8.99
      },
      { "category": "修真",
        "author": "南派三叔",
        "title": "星辰变",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "author": "老马",
      "color": "黑色",
      "price": 19.95
    }
  }
}
```

**解析语法**

| 语法 | 功能                         | 案例                                                         | 结果                                                         |
| ---- | ---------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| $    | 表示根元素，一般起始都会写   | -                                                            | -                                                            |
| *    | 通配符，表示所有元素         | jsonpath.jsonpath(obj,'$..*')                                | 返回根元素下所有元素                                         |
| ..   | 递归下降，该元素下的子孙元素 | jsonpath.jsonpath(obj,'$.store..price')                      | 返回store下所有的price                                       |
| [ ]  | 子元素操作符                 | jsonpath.jsonpath(obj,'$..book[2]')                          | 返回第三本书                                                 |
| ?( ) | 过滤                         | jsonpath.jsonpath.(obj,'&..book[?(@.isbn)]')<br />jsonpath.jsonpath(obj,'$..book[?(@.price>10)]') | 返回所有书中包含isbn的元素<br />返回所有书中price大于10的元素 |





## 下载数据



### 下载二进制文件

```python
import requests


# 二进制文件地址
url = 'https://www.keaidian.com/uploads/allimg/190424/24110307_35.jpg'


# 转为二进制文件
r = requests.get(url).content


# 下载 -- w后面加b写入的是二进制
with open('imp.jpg','wb') as f:
	f.write(r)
```



### 写入文本

```python
text = '文本内容'


# w是覆盖写入，a是在文本中追加
with open('filename.md','w',encoding='utf-8') as f: 
    f.write(text)
```
