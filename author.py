import json, sys, types, codecs, requests
inFile = sys.argv[1]

#site
url = 'http://dblp.uni-trier.de/search/publ/api'


outGeneralFile = codecs.open("general.out","w","utf-8")

with open(inFile) as data_file:
    professors = json.load(data_file)

for prof in professors["professors"]:
    params = dict(q=prof,h='1000',format='json')

    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)

    #outFile = codecs.open(prof+".out","w","utf-8")
    outGeneralFile.write(prof+"|")

    if 'hit' not in data['result']['hits']:
        print(prof)
    else:
        for i in data['result']['hits']['hit']:
            #outFile.write(prof+"|")
            #outFile.write(i['info']['title']+"|")
            #outGeneralFile.write(i['info']['title']+"|")
            author = i['info']['authors']['author']
            if isinstance(author, types.StringTypes):
                #outFile.write(author+"\n")
                #outGeneralFile.write(author+"|")
            else:
                for j in author:
                    if (j != prof):
                        #outFile.write(j+"|")
                        outGeneralFile.write(j+"|")
                #outFile.write("\n")
                #outGeneralFile.write("\n")

    #outFile.close()
    outGeneralFile.write("\n")
outGeneralFile.close()
