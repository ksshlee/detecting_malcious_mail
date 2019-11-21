# -*- coding: utf-8 -*-
import urllib.parse
import urllib.request
import json
import time


def get_result():
    #바이러스 토탈 api키 입력
    VT_KEY = 'd4488581e6ca8f7c1e8f2f355126b0f46844b906039887575e01fa7001946cf7'
    HOST = 'www.virustotal.com'
    SCAN_URL = 'https://www.virustotal.com/vtapi/v2/file/scan'
    REPORT_URL = 'https://www.virustotal.com/vtapi/v2/file/report'

    md5str=''

    #apikey 삽입
    fields = [('apikey', VT_KEY)]

    #virus토탈 결과값이 저장된곳
    txtf = open('virustotal_result.txt','r')

    #virustotal_result.txt에서  md5값만 추출해주기
    line = txtf.read()#전체 읽어오고

    cut_start = line.find("'md5': '")#md5가 포함된 문자열의 인덱스값 찾고
    cut_start_len = len("'md5': '")#그 길이 구하고
    cut_start = cut_start+cut_start_len#인덱스값에 길이 더하고
    cut_end = line.find("'",cut_start)#시작하는 인덱스 값 뒤에 "의 인덱스값 찾고
    md5str=line[cut_start:cut_end]#슬라이싱

    print(md5str)


    parameters = {'resource':md5str, 'apikey': VT_KEY}
    data = urllib.parse.urlencode(parameters).encode('utf-8')
    req = urllib.request.Request(REPORT_URL, data)
    response = urllib.request.urlopen(req)
    data = response.read()

    #데이터를 json 형태로 data변수에 저장.
    data = json.loads(data)

    #바이러스토탈에 응답값에서 필요한 Md5 scan결과 값 파싱
    md5 = data.get('md5', {})
    scan = data.get('scans', {})

    #바이러스 토탈에서 지원하는 백신 목록들
    keys = scan.keys()

    print(" ")
    print("==============바이러스 토탈 로딩중============")
    print("=========================================")

    if md5 =={}:
        print(" ********일치하는 값이 없습니다 **************")
    else:
        print("해당 파일의 해시값 : %s"%(md5))

    print("========================================")
    # time.sleep(20)#무료 api는 1분에 4개씩 제한이 있으므로 sleep을 시켜줍니다.


    for key in keys:
        if key=='FireEye' or key=='AhnLab-V3' or key=='ESET-NOD32' or key=='McAfee-GW-Edition' or key=='McAfee' or key=='Kaspersky' or key=='F-Secure':
            print('%-20s : %s' % (key,scan[key]['result']))

    txtf.close()
    print('===============끝===============')
