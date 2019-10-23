from tld import get_tld
from urllib.parse import urlparse
import whois
import re
# 1은 정상 0은 의심 -1은 피싱


def checklength(url):
    "url 길이 확인해주는 함수"
    if len(url)<54:
        return 1
    elif 54 <= len(url) <= 75:
        return 0
    else:
        return -1

def checkgolbange(url):
    "url에 @가 있는지 없는지 확인해주는 함수"
    if "@" in url:
        return -1
    return 1

def checkslash(url):
    "url에 -가 있는지 없는지 확인해주는 함수"
    if "-" in url:
        return -1
    return 1

def checkdoubleslash(url):
    "url에 추가적인 //가 있는지 확인"
    if "//" in url[7:]:
        return -1
    return 1

def checkipaddress(url):
    "url에 ip주소가 있는지 없는지 확인해주는 함수"
    text = (re.search('([0-9]{1,3})[.]([0-9]{1,3})[.]([0-9]{1,3})[.]([0-9]{1,3}.)', '{0}'.format(url)))
    if text == None:
        print('not phish')
        return

    print('phish')



def checkdomain(url):
    "url 에 도메인 개수 확인"
    domain_list=[".com", ".edu", ".gov", ".net", ".org", ".kr", ".jp", ".us", ".uk",  ".cn", ".fr", ".co.kr", "or.kr", "go.kr", "ac.kr"]

    res = get_tld(url,as_object=True)

    print(res.fld)
    
    if res.fld in domain_list:
        return 1
    return 0

def httpsorhttp(url):
    "http 인지 https인지 도출 요즘 은행, 비트코인 등 왠만한 거래들, 대기업 사이트들은 다 https에유"
    parts = urlparse('{0}'.format(url))
    if "https" in parts:
        return 1
    elif "http" in parts:
        return 0
    else:
        return -1


def checkport(url):
    "url에 포트있는지 없는지 확인"
    parts = urlparse('{0}'.format(url))
    if parts.port == None:
        return 1
    elif parts.port == 80 or parts.port == 443:
        return 0
    else :
        return -1

def checknetwork(url):
    "url 네트워크 위치 확인"
    parts = urlparse('{0}'.format(url))
    print(parts.netloc)

    print()
    

def urlwhois(url):
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

    if isinstance(domain_name, list):
        for dn in domain_name:
            passornot = False
            #this proccess is to find out the key and compare with values
            for flag in data.keys():
                if dn in data[flag]:
                    print("not phish!")
                    #if data have a same value with dn passornot is true
                    passornot = True 
                    break
            #if passornot is false
            if passornot == False:
                print('phish')
                return -1
    else :
        passornot = False
        #this proccess is to find out the key
        for flag in data.keys():
            if str(domain_name) in data[flag]:
                print('not phish!')
                passornot = True
                break
        if passornot == False:
            print('phish')
            return -1

    print("your flag is : %s" %(flag))
    
    if isinstance(creation_date, list):
        passornot = False
        for cd in creation_date:
            #find creation_date in same dictionary of domain_name
            if str(cd) in data[flag]:
                passornot = True
                print("not phish")
                return 1
        
        if passornot == False:
            print('phish')
            return 0
    else : 
        if str(creation_date) in data[flag]:
            print('not phish')
            return 1
        else:
            print('phish')
            return 0


    f.close()

url = 'www.digitalforensics.or.kr' #유현 강사님 사이트
url2 = 'www.naver.com'
url3 = 'https://www.citibank.co.kr/InsGuidDmnd0100.act?MENU_TYPE=pre&MENU_C_SQNO=M0_001830'
url4 = 'paypal.com-confirm-your-paypal-account.trainkook.com/Suspended-Account/Login/login?cmd=_signin&amp;dispatch=2e6f676ff44b310b672e8042a&amp;locale=en_US'
url5= 'https://banking.nonghyup.com'
url6 = 'https://naver.com//192.168.10.11'
url7 = 'https://www.google.com/search?newwindow=1&client=safari&rls=en&sxsrf=ACYBGNST4eiZh1HgmFAT9WEuQvIrHxydug%3A1571543348062&ei=NNmrXeW4A6Gh-Qakt6ygDg&q=naver.com&oq=naver.com&gs_l=psy-ab.3..35i39j0j0i10j0l7.494205.495130..495271...0.0..0.223.1034.6j2j1......0....1..gws-wiz.......0i131j0i67j0i20i263.VTcUam8Z4pA&ved=0ahUKEwjlooqY96nlAhWhUN4KHaQbC-QQ4dUDCAo&uact=5'
url8 = 'https://land.naver.com'
urlwhois(url8)