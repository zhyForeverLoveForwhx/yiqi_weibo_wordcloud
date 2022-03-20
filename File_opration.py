import csv
import time
from datetime import datetime


def save_result():
    File_Path = "D:\python_py\weibo_spider\weibo-search\结果文件\%23疫情%23"
    Filename = "%23疫情%23"
    CSV_Path = File_Path + "\\" + Filename + ".csv"
    Result_Path = 'result\\'+ Filename + "_result" + ".csv"
    EffectList = []
    Headers = []

    with open(CSV_Path, encoding='UTF-8')as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            if (len(Headers) == 0):
                Headers.append(row[1])
                Headers.append(row[4])
                Headers.append(row[12])
            else:
                EffectList.append([row[1], row[4], row[12]])

    with open(Result_Path, 'w', encoding='UTF-8-sig')as f:
        f_csv = csv.writer(f)
        f_csv.writerow(Headers)
        f_csv.writerows(EffectList)

def gettxt(filename,starttime,endtime):
    start = datetime.strptime(starttime, '%Y-%m-%d')
    end   = datetime.strptime(endtime  , '%Y-%m-%d')
    if starttime > endtime :
        print("初始时间大于结束时间")
        return
    result = []
    with open(filename, encoding='UTF-8')as fr:
        f_csv = csv.reader(fr)
        for row in f_csv:
            if len(row) == 0:
                continue
            try:
                rowtime = datetime.strptime(row[2]  , '%Y-%m-%d %H:%M')
            except ValueError:
                print("error",row[2])
                continue
            if start<= rowtime and end >= rowtime:
                result.append(row[1].replace('#疫情#','')+"\n")
            else:
                print("the time is out",rowtime)
    fr.close()
    save_filename = 'result\\'+ starttime + "--" + endtime +".txt"
    fw = open(save_filename,mode='w', encoding='UTF-8')
    fw.writelines(result)
    fw.close()

def removetag(a : str) -> str:
    return a.replace('#疫情#','')