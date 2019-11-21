import tkinter as tk
import email_parser as e
import get_hash_from_virustotal as get_hash
import virus_result as get_result

global string
string=""


def check_attachment(filename,filedirectory):
    get_hash.get_files_hash(filename,filedirectory)
    get_result.get_result()


def checkemail():
    _id = str(email_id.get())
    _passwd = str(email_passwd.get())
    result=e.checkemail(_id,_passwd)

    global string
    string=""

    file_name=""
    file_directory=""
    poped=result.pop()



    print(result)
    if len(result) == 0:
        string +="수신된 이메일이 없습니다."
        return

    
    if poped==1:#result의 맨뒤가 1이면 즉 첨부파일이랑 url이 없을떄
        print("메일 본문에 url과 첨부파일이 없습니다. \n\n\n")
        string+="메일 본문에 url과 첨부파일이 없습니다."
    elif poped==0:#result의 맨뒤가 0일때 즉 url 만있을때
        for i in result:
            print('%s의 사이트에서 %d 확률이 나왔습니다. 이유는 %s 와 같은 이유입니다.'%(i[0],i[1],i[2]))
            string+='%s의 사이트에서 %d 확률이 나왔습니다. 이유는 %s 와 같은 이유입니다.\n'%(i[0],i[1],i[2])
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
            string+='%s의 사이트에서 %d 확률이 나왔습니다. 이유는 %s 와 같은 이유입니다.\n'%(i[0],i[1],i[2])


        check_attachment(file_name,file_directory)
    



root = tk.Tk()
root.title('악성메일 탐지기')
root.geometry('300x300')

lbl1 = tk.Label(root, text='이메일').pack()
email_id = tk.Entry(root)
email_id.pack()
lbl2 = tk.Label(root, text='비밀번호')
email_passwd = tk.Entry(root)
email_passwd.pack()

btn = tk.Button(root, text='확인',command=checkemail).pack()

lbl3 = tk.Label(root, text='결과: \n')

def seeresult():
    global string
    print(string)
    lbl3['text']=string

resultbtn = tk.Button(root, text='결과보기', command=seeresult).pack()

lbl3.pack()


root.mainloop()