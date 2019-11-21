import whois


def push_data(url):
    string = ""

    try:
        data = whois.whois(url)
        domain_name = data.get('domain_name')
        creation_date = data.get('creation_date')
        #도메인 이름이 list형태일때
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

       

        f = open('data_set.txt','a') #데이터
        p = open('passeddata.txt','a') #passed 데이터


        f.write(url+" : ")

        if isinstance(domain_name,list):
            for dm in domain_name:
                f.write("%s   "%dm)
        else:
            f.write("%s   "%domain_name)
        if isinstance(creation_date,list):
            for cd in creation_date:
                f.write("%s   "%cd)
            f.write("\n")
        else:
            f.write("%s\n"%creation_date)
        
        string += url+" 데이터 추가완료"
    except:
        p.write(url+" = pass\n")
        string += url+" 데이터 추가실패"



    f.close()
    p.close()

    return string