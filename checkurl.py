from tld import get_tld
from urllib.parse import urlparse
import whois
from selenium import webdriver
import re
import datetime
# 1은 정상 0은 의심 -1은 피싱

def check_url_length(url):
    "url 길이 확인해주는 함수"
    if len(url)<54:
        return 2
    elif 54 <= len(url) <= 75:
        return 0
    else:
        return -1

def check_at_sign(url):
    "url에 @가 있는지 없는지 확인해주는 함수"
    if "@" in url:
        return -6
    return 3

def check_minus(url):
    "url에 -가 있는지 없는지 확인해주는 함수"
    if "-" in url:
        return -2
    return 2

def check_double_slash(url):
    "url에 추가적인 //가 있는지 확인"
    if "//" in url[7:]:
        return -4
    return 2

def check_ip_address_in_url(url):
    "url에 ip주소가 있는지 없는지 확인해주는 함수"
    text = (re.search('([0-9]{1,3})[.]([0-9]{1,3})[.]([0-9]{1,3})[.]([0-9]{1,3}.)', '{0}'.format(url)))
    if text == None:
        return 3

    return -9


def check_port_in_url(url):
    "url에 포트있는지 없는지 확인"
    parts = urlparse('{0}'.format(url))
    if parts.port == None:
        return 2
    elif parts.port == 80 or parts.port == 443:
        return 0
    else :
        return -4

# def check_if_shorten_url(url): not yet but soon will be update
#     if sorten:
#         return -10

def check_with_whois(url):
    "url whois 활용"
    f = open('data_set.txt', 'r') #open the data set
    line = f.read().splitlines()
    f.close()
    text=whois.whois('{0}'.format(url)) #save whois data in text
    domain_name=text['domain_name'] #domain_name of test url
    creation_date=text['creation_date'] #creation_date of test url
    #this proccess is making a data with dictionary
    data = {}
    for d in line:
        (key,value) = d.split(" : ")
        data[key] = value

    #if domain_name is list
    if isinstance(domain_name, list):
        for dn in domain_name:
            passornot = False
            #this proccess is to find out the key and compare with values
            for flag in data.keys():
                if dn in data[flag]:
                    #if data have a same value with dn passornot is true
                    passornot = True 
                    break
            #if passornot is false
            if passornot == False:
                return -1
    else :
        passornot = False
        #this proccess is to find out the key
        for flag in data.keys():
            if str(domain_name) in data[flag]:
                passornot = True
                break
        if passornot == False:
            return -1

    
    if isinstance(creation_date, list):
        passornot = False
        for cd in creation_date:
            #find creation_date in same dictionary of domain_name
            if str(cd) in data[flag]:
                passornot = True
                return 1
        
        if passornot == False:
            return 0
    else : 
        if str(creation_date) in data[flag]:
            return 1
        else:
            return 0

    f.close()


#to detect is it docs url
def cehck_if_docs(url):
    """구글 doc url인지 아닌지 판별해주는 함수"""
    if 'docs' in url:
        str= "it is docs url don't type important imformation if it is not sure"
        return str


def check_domain_creation(url):
    """도메인 생성날짜 알려주는 함수"""
    text=whois.whois(url)
    creation_date=text.get('creation_date')
    date=datetime.datetime.now()
    if isinstance(creation_date,list):
        for i in creation_date:
            if (date-i).days>=1095 and (date-i).days<1825:
                return -10
            elif (date-i).days<1095:
                return -20
    else:
        if (date-creation_date).days>=1095 and (date-creation_date).days<1825:
                return -10
        elif (date-creation_date).days<1095:
            return -20

    return 10



def define(url):
    sum =0

    checklist=[check_url_length,check_at_sign,check_minus,check_double_slash,check_ip_address_in_url,check_port_in_url,check_domain_creation] #checknetwork , checkdomain   is not complete yet httpsorhttp 성능 저하 유발로 일시 보류
    reasonphish=[] # to tell why it is phish
    result=[]


    result.append(url)
    
    if (check_with_whois(url)==1):
        sum+=100
    else:
        for i in checklist:
            sum+=i(url)
            if i(url)<=0 :
                reasonphish.append(str(i))

    if(sum==100):
        result.append(100)
    elif(sum<100 and sum>19):
        result.append(80)
    elif(sum<=19 and sum >=16):
        result.append(60)
    elif(sum<16 and sum >13):
        result.append(40)
    elif(sum<=13 and sum>=11):
        result.append(20)
    else:
        result.append(0)

    string=""

    for i in reasonphish:
        if 'check_url_length' in i:
            string+='Url 길이 초과 '
        if 'check_at_sign' in i:
            string+='@ 포함  '
        if 'check_minus' in i:
            string+='- 포함  '
        if 'check_double_slash' in i:
            string+='// 포함  '
        if 'check_ip_address_in_url' in i:
            string+='ip 주소 포함  '
        if 'httpsorhttp' in i:
            string+='because your url is http  '
        if 'check_port_in_url' in i:
            string+='포트번호 포함'
        if 'check_domain_creation' in i:
            string+="도메인 생성날짜 의심"

    #만약 결과가 100이라면
    if sum==100:
        result.append('피싱 사이트아님')
        return result

    #그외
    if len(string) == 0:
        result.append('걸린거없음')
        return result

    
    result.append(string)
    
    return result