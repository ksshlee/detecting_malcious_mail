import imaplib
import base64
import os
import email
import sys
import re

email_user = ('***@gmail.com') #이메일 주소
email_pass = ('**!') #이메일 비밀번호

mail = imaplib.IMAP4_SSL("imap.gmail.com","993") #주소와 포트번호

mail.login(email_user, email_pass) #로그인

mail.select('inbox') #받은 편지함 선택

type, data = mail.search(None, 'ALL') #'ALL'은 모든 메세지를 불러오고
#UNSEEN은 읽지 않은 메세지만 출력
#FROM "email"x
mail_ids = data[0] #데이터는 리스트이다
id_list = mail_ids.split() #mail_ids는 공간이 분리되어있는 string 형태
#mail_ids[-1]을 하게 되면 가장 최신의 메일 선택

for num in data[0].split():
    typ, data = mail.fetch(num, '(RFC822)' )
    raw_email = data[0][1]
# converts byte literal to string removing b''
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)

    #text = mail.fetch(num,"(UID BODY[TEXT])") #body이렇게도 호출 가능
   
    for response_part in data: # subject와 date를 받는 함수
            if isinstance(response_part, tuple):
                #print(email_message)
                msg = email.message_from_string(response_part[1].decode('utf-8'))
                email_subject = msg['subject']
                email_from = msg['from']
                email_date = msg['date']

                #email_body = msg['body']
                #print ('From : ' + email_from + '\n') #한글 이름이 인코딩 된 채로 나옴(정규화
                #시키면 가능
               
                from_split = email_from.split() #발신자
                try:
                    if email_from[0:5] == "=?UTF": #한글이 섞여있어 인코딩 된
                        #경우에만 디코딩 진행
                        from_split2 = from_split[0]                
                        from_split2 = from_split2[10:]
                        from_split2 = base64.b64decode(from_split2)
                        from_split2 = from_split2.decode('utf-8') # From base64디코드 후
                    #utf-8 디코드
                        print('From:' + from_split2 +" "+from_split[-1]+ '\n')
                    elif email_from[0:5] == "=?utf": #한글이 섞여있어 인코딩 된
                        #경우에만 디코딩 진행
                        from_split2 = from_split[0]                
                        from_split2 = from_split2[10:]
                        from_split2 = base64.b64decode(from_split2)
                        from_split2 = from_split2.decode('utf-8') # From base64디코드 후
                    #utf-8 디코드
                        print('From:' + from_split2 +" "+from_split[-1]+ '\n')
                    else:
                        from_split2 = email_from #영어는 그대로 출력
                        print('From:' + from_split2+'\n')
                except:
                    pass

                try:
                    if email_subject[0:5] == "=?UTF": #제목
                        #한글이 섞여있어 인코딩 된 경우에만 디코딩 진행
                        subject_split = email_subject[10:] # Subject 디코딩
                        subject_split = base64.b64decode(subject_split)
                        subject_split = subject_split.decode('utf-8')
                       
                    elif email_subject[0:5] == "=?utf": #제목
                        #한글이 섞여있어 인코딩 된 경우에만 디코딩 진행
                        subject_split = email_subject[10:] # Subject 디코딩
                        subject_split = base64.b64decode(subject_split)
                        subject_split = subject_split.decode('utf-8')
                    else:
                        subject_split = email_subject #영어는 그대로 출력
                           
                    print ('Subject : ' + subject_split + '\n')
                    print('Date : ' + email_date + '\n')
                except:
                    pass
                body = "default"
                try:
                    for part in email_message.walk(): #text body를 출력하는 함수
                        if part.get_content_type() == "text/plain":
                            body = part.get_payload(decode=True)
                            p_body = body.decode('utf-8')
                            body = p_body
                            print('Body : ' + p_body)
                           
                           
                   
                    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', body)
                    print("URL: ")
                    print(urls)
     
                except:
                    pass
               
    try:
        for part in email_message.walk(): #첨부파일을 다운받는 함수
                if part.get_content_maintype() == 'multipart':
                    continue
                if part.get('Content-Disposition') is None:
                    continue
                fileName = part.get_filename()

                if fileName[0:5] == "=?UTF":
                    file_split = fileName[10:]
                    file_split = base64.b64decode(file_split)
                    file_split = file_split.decode('utf-8')
                elif fileName[0:5] == "=?utf":
                    file_split = fileName[10:]
                    file_split = base64.b64decode(file_split)
                    file_split = file_split.decode('utf-8')
                else:
                    file_split = fileName

                if bool(file_split):
                    filePath = os.path.join('/Users/zeros/Downloads', file_split)
                    if not os.path.isfile(filePath) :
                        fp = open(filePath, 'wb')
                        fp.write(part.get_payload(decode=True))
                        fp.close()
               
                    print(file_split + " 첨부파일을 다운로드 하였습니다")
                    print("\n"+"\n")
                    print('----------------------------------')
    except:
        pass
