from tld import get_tld
from urllib.parse import urlparse
import whois
from selenium import webdriver
import re
# 1은 정상 0은 의심 -1은 피싱

def checklength(url):#checked
    "url 길이 확인해주는 함수"
    if len(url)<54:
        return 2
    elif 54 <= len(url) <= 75:
        return 0
    else:
        return -1

def checkgolbange(url):#checked
    "url에 @가 있는지 없는지 확인해주는 함수"
    if "@" in url:
        return -6
    return 3

def checkslash(url):#checked
    "url에 -가 있는지 없는지 확인해주는 함수"
    if "-" in url:
        return -2
    return 2

def checkdoubleslash(url):#checked
    "url에 추가적인 //가 있는지 확인"
    if "//" in url[7:]:
        return -4
    return 2

def checkipaddress(url):#checked
    "url에 ip주소가 있는지 없는지 확인해주는 함수"
    text = (re.search('([0-9]{1,3})[.]([0-9]{1,3})[.]([0-9]{1,3})[.]([0-9]{1,3}.)', '{0}'.format(url)))
    if text == None:
        return 3

    return -9



def httpsorhttp(url):#checked
    "http 인지 https인지 도출 요즘 은행, 비트코인 등 왠만한 거래들, 대기업 사이트들은 다 https에유"
    if 'https' in url or 'http' in url:
        pass
        #url='http'+url
    else:
        url='http://'+url



    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome('./chromedriver', chrome_options=options)
    driver.get(url) #Trying http first
    url = driver.current_url

    if(url[:url.find(":")]=='https'):
        return 3


    return -4


def checkport(url):#checked
    "url에 포트있는지 없는지 확인"
    parts = urlparse('{0}'.format(url))
    if parts.port == None:
        return 2
    elif parts.port == 80 or parts.port == 443:
        return 0
    else :
        return -4

# def shortenurl(url): not yet but soon will be update
#     if sorten:
#         return -10

def urlwhois(url):#checked
    "url whois 활용"
    f = open('test.txt', 'r') #open the data set
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
def ifdocs(url):
    if 'docs' in url:
        str= "it is docs url don't type important imformation if it is not sure"
        return str




def define(url):
    sum =0

    checklist=[checklength,checkgolbange,checkslash,checkdoubleslash,checkipaddress,checkport] #checknetwork , checkdomain   is not complete yet httpsorhttp 성능 저하 유발로 일시 보류

    reasonphish=[] # to tell why it is phish

    if (urlwhois(url)==1):
        sum+=100
    else:
        for i in checklist:
            sum+=i(url)
            if i(url)<=0 :
                reasonphish.append(str(i))
    

    reasonphish.append(sum)

    return reasonphish

    # for i in reasonphish:
    #     if 'checklength' in i:
    #         print('beacuse of your length!')
    #     if 'checkgolbange' in i:
    #         print('beacuse your url include @')
    #     if 'checkslash' in i:
    #         print('beacuse your url include -')
    #     if 'checkdoubleslash' in i:
    #         print('because your url include //')
    #     if 'checkipaddress' in i:
    #         print('because your url contains ip address')
    #     if 'httpsorhttp' in i:
    #         print('because your url is http')
    #     if 'checkport' in i:
    #         print('your url have port')
