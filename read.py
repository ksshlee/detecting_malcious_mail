import whois

f = open('data.txt','r')

while True:    
    data= f.read().splitlines()
    if not data:
        break
    for rst in data:
        print(rst)
        try:
            a = open('test.txt','a')
            ans = whois.whois('{0}'.format(rst))
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
                a.write("%s   \n"%ans['creation_date'])
        except :
            a.write(rst+" = pass\n")
            