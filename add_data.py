import whois


def push_data(url):

    p = open('passeddata.txt','a') #passed 데이터

    string = ""

    try:
        data = whois.whois(url)
        domain_name = data.get('domain_name')
        creation_date = data.get('creation_date')

        #도메인 이름이나 생성날짜가 none일때 예외 발생

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


                 
        #중복검사
        f = open('data_set.txt','r') #데이터를  불러오기 위해 잠깐 읽기모드로
        line = f.read().splitlines()
        f.close()
        #데이터들을 리스트로 변환
        data_for_check_duplication = {}
        for d in line:
            (key,value) = d.split(" : ")
            data_for_check_duplication[key] = value

        #추가하고 싶은 데이터의 도메인 이름과 저장되어 있는 데이터에서 도메인 이름 즁복검사
        if isinstance(domain_name, list):
            for dn in domain_name:
                for flag in data_for_check_duplication.keys():
                    if dn in data_for_check_duplication[flag]:
                        string=url+"는 이미 존재하는 데이터입니다."
                        return string

        else :
            for flag in data.keys():
                if str(domain_name) in data[flag]:
                    string=url+"는 이미 존재하는 데이터 입니다."
                    return string




        #none 예외 통과 및 중복 검사 통과후
        f = open('data_set.txt','a') #데이터
        

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

        f.close()

    except:
        #예외처리시
        p.write(url+" = pass\n")
        string += url+" 데이터 추가실패"
        p.close()

    

    return string