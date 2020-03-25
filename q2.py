
from pymongo import MongoClient
import re
import time
count = 1
for i in range(1996,2021):
    print(i)
    f = open(str(i) + '.txt', 'r+', encoding='utf-8')
    lines = f.readlines()
    ls=[]
    ls1=[]
    for line in lines:
        ls.append(line)
    for index,line in enumerate(ls):
        print(index,line)
        if '[Language:' in line:
            ls.pop(index-1)

    print(ls)

    for line in ls:

        if re.findall(r'(\w+?)(\s+)(\d)', str(line)):
                if 'by' in str(line):
                    strings = re.sub(r'\d+', '', line)
                    print(strings)
                    bookname = strings.split('by')[0]
                    bookname = re.sub(r',', '', bookname)
                    authorname = strings.split('by')[1]
                    print(count)
                    count = count + 1
                   # time.sleep(0.001)
                    print("Bookname:", bookname)
                    print("Author name:", authorname)
                    client = MongoClient('mongodb://localhost:27017')
                    db = client.cloud.bookinventory
                    
                    db.insert_one(
                        {"Bookname": bookname,
                         "Authorname": authorname,

                         }
                    )








