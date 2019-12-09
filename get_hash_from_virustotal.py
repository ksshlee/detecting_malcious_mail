import json
import sys
import requests

def FileScan(filepath,apikey,url):
        params = {'apikey':apikey}
        files = {'file' : (open(filepath, 'rb'))}
        response= requests.post(url, files = files, params = params)
        return response.json()


def get_files_hash(files_name,files_path):
    url = 'http://www.virustotal.com/vtapi/v2/file/scan'
    file_path = files_path #경로
    file_name = files_name #분석할파일이름
    api_key = 'd4488581e6ca8f7c1e8f2f355126b0f46844b906039887575e01fa7001946cf7'

    response = FileScan(file_path, api_key,url)
    f = open('virustotal_result.txt', 'w')
    f.write(str(response))
    f.close()