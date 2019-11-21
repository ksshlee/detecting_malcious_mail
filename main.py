import tkinter as tk
import email_parser as e
import get_hash_from_virustotal as get_hash
import virus_result as get_result
import add_data

global string_for_email_result
string_for_email_result=""

global string_for_add_data_result
string_for_add_data_result=""


#사용자가 원하는 url 도메인 데이터 추가해주는 함수
def add_domain_data():
    global string_for_add_data_result
    string_for_add_data_result="" #결과 도출할 변수 초기화
    url = str(new_url.get())
    string_for_add_data_result=add_data.push_data(url)



#첨부파일 확인해주는 함수
def check_attachment(filename,filedirectory):
    global string_for_email_result
    get_hash.get_files_hash(filename,filedirectory)#파일 해시
    string_for_email_result+=get_result.get_result()#파일 검사 결과



#이메일 확인
def checkemail():
    _id = str(email_id.get())
    _passwd = str(email_passwd.get())
    result=e.checkemail(_id,_passwd)

    global string_for_email_result
    string_for_email_result=""

    file_name=""
    file_directory=""
    poped=result.pop()



    if len(result) == 0:
        string_for_email_result +="수신된 이메일이 없습니다."
        return

    
    if poped==1:#result의 맨뒤가 1이면 즉 첨부파일이랑 url이 없을떄
        print("메일 본문에 url과 첨부파일이 없습니다. \n\n\n")
        string_for_email_result+="메일 본문에 url과 첨부파일이 없습니다."
    elif poped==0:#result의 맨뒤가 0일때 즉 url 만있을때
        for i in result:
            print('%s의 사이트에서 %d 확률이 나왔습니다. 이유는 %s 와 같은 이유입니다.'%(i[0],i[1],i[2]))
            string_for_email_result+='%s의 사이트에서 %d 확률이 나왔습니다. 이유는 %s 와 같은 이유입니다.\n'%(i[0],i[1],i[2])
    elif poped==-1:#-1일때 즉 첨부파일만 있을때
        for i in result:
            file_name = i.get('filename')#첨부파일 이름 추출
            file_directory = './Downloads/'+file_name#첨부파일이 포함된 디렉토리

        check_attachment(file_name,file_directory)
    elif poped==-2:#-2일때 즉 둘다 있을때
        for i in result:
            if isinstance(i,dict)==True:#리스트 안에 dict 형태 즉 첨부파일 이름이 포함되어 있으면
                file_name = i.get('filename')#첨부파일 이름 추출
                file_directory = './Downloads/'+file_name#첨부파일이 포함된 디렉토리
                continue
            print('%s의 사이트에서 %d 확률이 나왔습니다. 이유는 %s 와 같은 이유입니다.'%(i[0],i[1],i[2]))
            string_for_email_result+='%s의 사이트에서 %d 확률이 나왔습니다. 이유는 %s 와 같은 이유입니다.\n'%(i[0],i[1],i[2])


        check_attachment(file_name,file_directory)
    



root = tk.Tk()
root.title('악성메일 탐지기')
root.geometry('300x300')


#이메일, 비밀번호 입력 영역
label_for_email = tk.Label(root, text='이메일').pack()
email_id = tk.Entry(root)
email_id.pack()
label_for_passwd = tk.Label(root, text='비밀번호')
email_passwd = tk.Entry(root)
email_passwd.pack()

btn_for_check_mail = tk.Button(root, text='확인',command=checkemail).pack()



#이메일결과 도출 영역
label_for_email_result = tk.Label(root, text='결과: \n')

def see_email_result():
    global string_for_email_result
    label_for_email_result['text']=string_for_email_result

btn_for_email_result = tk.Button(root, text='결과보기', command=see_email_result).pack()

label_for_email_result.pack()





#데이터 추가 영역
label_for_push_data = tk.Label(root, text='추가하고 싶은 도메인(url형태)').pack()

new_url = tk.Entry(root)
new_url.pack()

btn_for_push_data = tk.Button(root, text='데이터 삽입',command=add_domain_data).pack()



#도메인 데이터 추가 결과 도출 영역
label_for_addingdata_result = tk.Label(root, text='결과: \n')

def see_addingdata_result():
    global string_for_add_data_result
    label_for_addingdata_result['text']=string_for_add_data_result

btn_for_addingdata_result = tk.Button(root, text='결과보기', command=see_addingdata_result).pack()

label_for_addingdata_result.pack()

root.mainloop()