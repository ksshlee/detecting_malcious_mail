import whois

f = open('data.txt','r')
a = open('ohoho.txt','a') # save a data
p = open('oohohpass.txt','a') #save a passed data

data= f.read().splitlines() 
for rst in data:
    print(rst)
    try:
        ans = whois.whois('{0}'.format(rst))
        #도메인 이름이나 생성날짜가 none일때 예외 발생

        #도메인 이름이 list형태일때
        domain_name = ans.get('domain_name')
        creation_date = ans.get('creation_date')
        if(isinstance(domain_name,list)):
            for i in domain_name:
                if i is None:#domain이름이 none일때 예외 발생
                    raise
        else:
            if domain_name is None:
                raise
        
        #생성날짜가 list 형태일때
        if(isinstance(creation_date,list)):
            for i in creation_date:
                if i is None:#생성날짜가 none일때 예외 발생
                    raise
        else:
            if creation_date is None:
                raise

        a.write(rst+" : ")
        if type(ans['domain_name']) is list:
            for dm in ans['domain_name']:
                a.write("%s   " % dm)
        else :
            a.write("%s  "%ans['domain_name'])
        if type(ans['creation_date']) is list:
            for cd in ans['creation_date']:
                a.write('%s   ' % cd)
            a.write('\n')
        else:
            a.write("%s\n"%ans['creation_date'])
    except :
        p.write(rst+" = pass\n")
    
f.close()
a.close()
p.close()