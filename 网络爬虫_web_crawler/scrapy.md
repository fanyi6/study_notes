# Scrapy爬虫工具

Scrapy是一个为了爬取网站数据，提取结构性数据而编写的应用框架。 可以应用在包括数据挖掘，信息处理或存储历史数据等一系列的程序中



## 安装scrapy

```
pip install scrapy

安装过程中出错:

如果安装有错误!!!!
pip install Scrapy
building 'twisted.test.raiser' extension
error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++
Build Tools": http://landinghub.visualstudio.com/visual‐cpp‐build‐tools 
解决方案:
http://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted 下载twisted对应版本的whl文件(如我的Twisted‐17.5.0‐cp36‐cp36m‐win_amd64.whl)，cp后面是
python版本，amd64代表64位，运行命令:
pip install C:\Users\...\Twisted‐17.5.0‐cp36‐cp36m‐win_amd64.whl pip install Scrapy


如果再报错
python ‐m pip install ‐‐upgrade pip 

如果再报错 win32
解决方法:
pip install pypiwin32 

再报错:使用anaconda
使用步骤: 打开anaconda
点击environments
点击not installed
输入scrapy
apply 在pycharm中选择anaconda的环境
```



## 创建scrapy项目

考虑到未知多页下载的需求，这里借用CrawlSpider，除了网页构建不同其他基本相同

本次演示以电影天堂国内电影区为例：https://www.ygdy8.net/html/gndy/china/list_4_1.html

```python
# 终端 -- 进入到需要创建的爬虫文件夹下
cd 爬虫文件夹路径


# 终端 -- 创建scrapy项目
scrapy startproject 项目名称 # 不能数字开头


# 终端 -- 跳转到spiders文件夹，创建爬虫文件
cd 目录名字/目录名字/spiders
scrapy genspider ‐t crawl 爬虫名字 网页的域名
scrapy genspider ‐t crawl 


# 终端 -- 运行爬虫文件方法
scrapy crawl 爬虫名称
```



**创建的爬虫项目目录如下**

```python
├── scrapy.cfg # 项目配置文件
└── 项目名称 # 项目python模块, 之后将在此加入代码 -- 我这里创建的名为movie，后面演示将用movie
    ├── __init__.py
    ├── items.py # 项目items文件
    ├── pipelines.py # 项目管道文件
    ├── settings.py # 项目配置文件
    └── spiders # 放置spider的目录
        └── __init__.py
        └── 自己创建的爬虫文件.py # 我这里创建的名为md，后面演示将用md
```





## scrapy工作原理

![image-20220405210621049](/Users/Zander/Typora库/img/image-20220405210621049.png)

![image-20220405210633381](/Users/Zander/Typora库/img/image-20220405210633381.png)



## 网页请求解析数据

创建好项目之后进入python爬虫项目，打开spiders，进入创建的爬虫文件，我这里名为md

本次演示地址：https://www.ygdy8.net/html/gndy/china/list_4_1.html



### 校验文件修改配置

**首先进入md文件调整检验项目可以正常运行**

```python
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MdSpider(CrawlSpider):
    name = 'md' # 项目名字
    allowed_domains = ['www.ygdy8.net'] # 允许访问的地址 -- 这里只包含域名
    start_urls = ['https://www.ygdy8.net/html/gndy/china/list_4_1.html'] # 声明一个起始地址 -- 修改成具体请求地址

    rules = (
        Rule(LinkExtractor(allow=r'https://www.ygdy8.net/html/gndy/china/list_4_\d+.html'), callback='parse_item', follow=True),
    ) # 正则获取所有页，编写allow规则

    def parse_item(self, response): # 输入print()运行文件查询是否可以正常运行
        print('============================')
        

# 终端 -- 爬虫文件运行
scrapy crawl md
```

**如果正常运行则进入下一步，不可以正常运行则进入settings将ROBOTSTXT_OBEY = True注释掉**

```python
# ROBOTSTXT_OBEY = True
```



### 解析数据

本次请求获取https://www.ygdy8.net/html/gndy/china/list_4_1.html的电影名及子页面的图片，获取全部页面

```python
# md.py文件

from movie.items import MovieItem # 导入items


    def parse_item(self, response): # 输入print()运行文件查询是否可以正常运行
        # print('============================')
        # name = response.xpath('//div[@class="co_content8"]//td[2]//a[2]/text()')
        # href = response.xpath('//div[@class="co_content8"]//td[2]//a[2]/@href')

        a_list = response.xpath('//div[@class="co_content8"]//td[2]//a[2]')

        for a in a_list:
            # 获取第一页的name 和 要点击的链接
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()


            url = 'https://www.ygdy8.net' + href # 拼接图片页请求地址

            # 访问parse_second，同时将name和state传入
            yield scrapy.Request(url=url,callback=self.parse_second,meta={'name':name})


    def parse_second(self,response): # 模仿parse_item()

        # src = response.xpath('//div[@class="co_content8"]//img/@src').extract_first() # 获取图片地址
        src = response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
        name = response.meta['name'] # 接收传来的name


        movie = MovieItem(name=name,src=src) # 传入items

        yield movie 
```



## 传到items

```python
# items.py

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field() # 名字不能乱起要和传入数据对应
    src = scrapy.Field()
```



## 数据存储下载



### 存储数据到json文件

**首先在settings打开管道**

```python
# settings,py

# 将原本被注释的ITEM_PIPELINES恢复
ITEM_PIPELINES = {
   'movie.pipelines.MoviePipeline': 300,
}
```

**储存数据到json文件**

```python
from itemadapter import ItemAdapter


class MoviePipeline:

    def open_spider(self,spider): # 打开一个json文件
        self.f = open('movies.json','w',encoding='utf-8')

    def process_item(self, item, spider): # 持续写入item -- 需要用str转
        self.f.write(str(item))
        return item

    def close_spider(self,spider): # 关闭文件
        self.f.close()
```



### 多管道下载图片

**模仿MoviePipeline在下方创建一个下载图片的类PhotoDown，将之加入到settings**

```python
# settings.py

ITEM_PIPELINES = {
   'movie.pipelines.MoviePipeline': 300, # 数字代表优先级
   'movie.pipelines.PhotoDown':301 # 数字小的先执行
}
```



**将图片下载到本地**

```python
import requests


class PhotoDown:

        def process_item(self, item, spider):
            name = item.get('name')
            src = item.get('src')
           

            r = requests.get(src).content
            with open('./moviephoto/' + name +'.jpg','wb') as f:
                f.write(r)
                return item
```



### 数据写入到数据库

**setting配置参数**

```python
# setting.py


# 在setting中加入下面数据
DB_HOST = '192.168.231.128' # 数据库ip
DB_PORT = 3306 # 默认端口不变
DB_USER = 'root' # 数据库用户名
DB_PASSWORD = '1234' # 数据库密码
DB_NAME = 'test' # 数据库名字
DB_CHARSET = 'utf8' # 编码
```



**管道配置**

```python
# pipelines.py


from scrapy.utils.project import get_project_settings
import pymysql


class MysqlPipeline:

    
    # __init__方法和open_spider的作用是一样的
    # init是获取settings中的连接参数
    def open_spider(self,spider):
        settings = get_project_settings()
        self.host = settings['DB_HOST']
        self.port =settings['DB_PORT']
        self.user =settings['DB_USER']
        self.password =settings['DB_PASSWROD']
        self.name =settings['DB_NAME']
        self.charset =settings['DB_CHARSET']

        self.connect()
        
        
	# 连接数据库并且获取cursor对象
    def connect(self):
        self.conn = pymysql.connect(
                            host=self.host,
                            port=self.port,
                            user=self.user,
                            password=self.password,
                            db=self.name,
                            charset=self.charset
        )

        self.cursor = self.conn.cursor()


    def process_item(self, item, spider):

        sql = 'insert into book(name,src) values("{}","{}")'.format(item['name'],item['src']) # 传入数据库
        # 执行sql语句
        self.cursor.execute(sql)
        # 提交
        self.conn.commit()

        return item


    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
```



## post请求

eg：百度翻译：https://fanyi.baidu.com/translate?aldtype=16047&query=final&keyfrom=baidu&smartresult=dict&lang=auto2zh#en/zh/final

```python
import scrapy
import json


class TestpostSpider(scrapy.Spider):
    name = 'testpost'
    allowed_domains = ['https://fanyi.baidu.com/sug']
    # post请求 如果没有参数 那么这个请求将没有任何意义
    # 所以start_urls 也没有用了
    # parse方法也没有用了
    # start_urls = ['https://fanyi.baidu.com/sug/']
    #
    # def parse(self, response):
    #     pass

    def start_requests(self): # 准备参数
        url = 'https://fanyi.baidu.com/sug'

        data = {
            'kw': 'final'
        }

        yield scrapy.FormRequest(url=url,formdata=data,callback=self.parse_second)

    
    # 重写parse方法，传入data
    def parse_second(self,response):

        content = response.text
        obj = json.loads(content,encoding='utf-8')

        print(obj)
```





## 代理

```python
# settings.py

# 到settings.py中，打开一个选项 
DOWNLOADER_MIDDLEWARES = {
              'postproject.middlewares.Proxy': 543,
           }
```

```python
# 到middlewares.py中写代码

def process_request(self, request, spider):
               request.meta['proxy'] = 'https://113.68.202.10:9999'
               return None
```
