import json
import sys
import requests

url = 'http://www.virustotal.com/vtapi/v2/file/scan'
file_path = './Downloads/linkedlistandarray.docx' #경로
file_name = 'linkedlistandarray.docx' #분석할파일이름
api_key = 'd4488581e6ca8f7c1e8f2f355126b0f46844b906039887575e01fa7001946cf7'

def FileScan(filepath,apikey):
    params = {'apikey':apikey}
    files = {'file' : (open(filepath, 'rb'))}
    response= requests.post(url, files = files, params = params)
    return response.json()


response = FileScan(file_path, api_key)

sys.stdout = open('virustotal_result.txt', 'w+')
print(file_path + ' '+ json.dumps(response, indent = 4))
sys.stdout = open('virustotal_result.txt','w+')