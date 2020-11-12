import requests
import json
import datetime
import time
from jsonpath import jsonpath

def date_change():#定义时间累加函数

    global start_date
    
    td = datetime.timedelta(days=1) #累加1天
    final_date = start_date + td
    d = final_date.__format__('%Y-%m-%d')
    return d

def url_get():#金山词霸每日一句接口网址拼接

    url1 = "http://api.tianapi.com/txapi/lunar/index?key=xxxxxxxxxx&date="#key 请在天行数据官网申请，api接口也是用他们的
    url2 = date_change()

    url = url1 + url2
    return url

def info_get():#爬取信息，并提取json，写入文档

    url_fin = url_get()

    html = requests.get(url_fin)
    
    jsonData = html.text

    s=json.loads(jsonData)
    
    gregoriandate = jsonpath(s,"*..gregoriandate")[0]
    lunar_festival = jsonpath(s,"*..lunar_festival")[0]
    fitness = jsonpath(s,"*..fitness")[0]
    taboo =jsonpath(s,"*..taboo")[0]
    tiangandizhiyear = jsonpath(s,"*..tiangandizhiyear")[0]
    tiangandizhimonth = jsonpath(s,"*..tiangandizhimonth")[0]
    tiangandizhiday = jsonpath(s,"*..tiangandizhiday")[0]
    lmonthname = jsonpath(s,"*..lmonthname")[0]
    lubarmonth = jsonpath(s,"*..lubarmonth")[0]
    lunarday = jsonpath(s,"*..lunarday")[0]
    festival = jsonpath(s,"*..festival")[0]
    jieqi = jsonpath(s,"*..jieqi")[0]
    data = ["*",gregoriandate,"","^",festival,"^",fitness,"^",taboo,"^",tiangandizhiyear,"年 ",tiangandizhimonth,"月 ",tiangandizhiday,"日 ","^",lmonthname,"^",lubarmonth,lunarday," ",jieqi," ",lunar_festival,"\n"]

    with open("data.txt",'a',encoding="utf-8") as f:
        f.writelines(data)
    return

if __name__ == '__main__':
    
    start_date = datetime.date(2020,12,31)
    
    for i in range(1,366):
        info_get()
        print (date_change())
        start_date = datetime.datetime.strptime(date_change(), "%Y-%m-%d")
        #time.sleep (1)
        
