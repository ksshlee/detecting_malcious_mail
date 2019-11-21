import whois



def add_data(url):
    f = open('data_set.txt','a') #데이터를 추가할곳
    p = open('passeddata.txt','a') #passed 데이터

    string = ""

    try:
        data = whois.whois(url)
        domain_name = data.get('domain_name')
        creation_date = data.get('creation_date')
        if('None' in domain_name or 'None' in creation_date): #None이 들어가있으면 예외 처리
            raise

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

add_data('toss.io')