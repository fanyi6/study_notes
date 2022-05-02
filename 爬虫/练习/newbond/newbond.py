from email import header
from webbrowser import get
import requests
import json
import jsonpath
import datetime


def Retrieve_Data():
        
    # 获取请求地址
    url = 'https://datacenter-web.eastmoney.com/api/data/v1/get?callback=jQuery1123012885897749515896_1649336091023&sortColumns=PUBLIC_START_DATE&sortTypes=-1&pageSize=50&pageNumber=1&reportName=RPT_BOND_CB_LIST&columns=ALL&quoteColumns=f2~01~CONVERT_STOCK_CODE~CONVERT_STOCK_PRICE%2Cf235~10~SECURITY_CODE~TRANSFER_PRICE%2Cf236~10~SECURITY_CODE~TRANSFER_VALUE%2Cf2~10~SECURITY_CODE~CURRENT_BOND_PRICE%2Cf237~10~SECURITY_CODE~TRANSFER_PREMIUM_RATIO%2Cf239~10~SECURITY_CODE~RESALE_TRIG_PRICE%2Cf240~10~SECURITY_CODE~REDEEM_TRIG_PRICE%2Cf23~01~CONVERT_STOCK_CODE~PBV_RATIO&source=WEB&client=WEB'

    # 获取请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        'Cookie': 'JSESSIONID=DA062E36B51EC69481EC55EA23336E73; qgqp_b_id=07e364420df0ba22c7e879b4c301457d; st_si=57390423987380; st_pvi=58160804671209; st_sp=2022-04-07%2020%3A54%3A38; st_inirUrl=; st_sn=1; st_psi=20220407205438163-113300300986-9368149090; st_asi=delete'
    }

    # 获取响应数据
    response= requests.get(url=url,headers=headers).text

    response = response.split('(',1)[1].rsplit(')',1)[0] # 将响应数据截取需要的部分

    # 将数据保存到json文件
    with open('xz.json','w') as f:
        f.write(response)


def Judge():

    obj = json.load(open('xz.json','r',encoding='utf-8')) # 获取json数据

    ret = jsonpath.jsonpath(obj,'$..data.*') # 获取所有数据

    # 获取当天日期
    today = str(datetime.date.today())
    a = 0
    # 判断出还未上市的可转债
    for i in ret:
        xz_time = i['VALUE_DATE'][:10] # 提取获取数据中可转债上市日期
        if xz_time == today: # 判断那个当天上市
            name = i['SECURITY_NAME_ABBR']
            code = i['SECURITY_CODE']
            print(name,code)
            a +=1

    if a== 0:
        print('当日无新债')
    
            



if __name__ == '__main__':
    # 获取可转债数据储存
    Retrieve_Data()
    # 判断当日上市的可转债
    Judge()