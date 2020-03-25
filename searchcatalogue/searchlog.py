import time
dict1 = dict()

def searchlogg(keyword,time):

    words = keyword.split()
    t=str(time)
    for word in words:
        if word in dict1:
            dict1[word] += 1
        else:
            dict1[word] = 1
    print(dict1)
    f = open('logfile.txt', 'w+')

    for key, value in dict1.items():
        print(key, value)
        f.write(key + "  " + str(value) + '  ' + t + '\n')
    f.close()



