# -*- coding:utf-8 -*-
import json

def getEP(filename):
    with open(filename, 'r', encoding='UTF-8') as fp1:
        # print(fp.read())
        fpd = json.loads(fp1.read())
    #     i = 0
    #     while fpd['roster'][i]:
    #         print('{0} '.format(i+1))
    #         print(fpd['roster'][i])
    #         i+=1
    EPlist = {} 
    for d in fpd['roster']:
        # print(d)
        EPlist.update({d[0]:d[3]}) 
    # print(list(fpd['roster'][0][3]))
    # print(fpd['roster'][0][3:1:1])
    # dict1 = dict(zip(fpd['roster'][0][0:1:1],fpd['roster'][0][3:1:1]))
    return EPlist
    # print(dict1)
    
def getchecklist():
    with open('checklist.txt', 'r', encoding='UTF-8') as fp2:
        cl = fp2.readlines()
    return cl

  


if __name__ == '__main__':
    try:
        weeknum = input('输入本周周数（例：52）：')
        # filename = input('输入本周文件名（例：2020-50.json）：')
        lastweek = getEP('2020-{0}.json'.format(int(weeknum)-1))
        print(lastweek)

        currentEP = getEP('2020-{0}.json'.format(int(weeknum)))
        checklist = getchecklist()
        # print(checklist)
        for n in checklist:
            print('{0}:{1}'.format(n[:-1],lastweek[n[:-1]]))
        for m in checklist:
            print('{0}:{1}'.format(m[:-1],currentEP[m[:-1]]))   
    except Exception as e:
        print(e)