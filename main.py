import tkinter as tk
import email_parser as e

def checkemail():
    _id = str(email_id.get())
    _passwd = str(email_passwd.get())
    print(e.checkemail(_id,_passwd))



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

root.mainloop()