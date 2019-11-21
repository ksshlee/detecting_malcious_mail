import whois

f = open('data.txt','r')
a = open('data_set.txt','a') # save a data
p = open('passeddata.txt','a') #save a passed data

data= f.read().splitlines() 
for rst in data:
    print(rst)
    try:
        ans = whois.whois('{0}'.format(rst))
        # if ('None' in ans['domain_name'] or 'None' in ans['creation_date']):
        #     raise

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