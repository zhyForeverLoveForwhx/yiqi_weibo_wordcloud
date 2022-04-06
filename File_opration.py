import csv
import os
import time
from datetime import datetime
from os import path

# import pathlib


save_model = 'a'

def save_result(Filename:str,resultpath :str,datapath:str):
    #dir = path.dirname(__file__)
    CSV_Path = datapath + Filename + ".csv"
    Result_Path = resultpath + Filename + "_result" + ".csv"
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
        f.close()

    with open(Result_Path, 'w', encoding='UTF-8-sig')as f:
        f_csv = csv.writer(f)
        f_csv.writerow(Headers)
        f_csv.writerows(EffectList)
        f.close()

def gettxt(filepath:str,filename:str,starttime:str,endtime:str):
    start = datetime.strptime(starttime, '%Y-%m-%d')
    end   = datetime.strptime(endtime  , '%Y-%m-%d')
    if starttime > endtime :
        print("初始时间大于结束时间")
        return
    result = []
    totalpath = filepath + filename
    with open(totalpath, encoding='UTF-8')as fr:
        f_csv = csv.reader(fr)
        for row in f_csv:
            if len(row) == 0:
                continue
            try:
                rowtime = datetime.strptime(row[2]  , '%Y-%m-%d %H:%M')
            except ValueError:
                print("time error",row[2])
                continue
            if start<= rowtime and end >= rowtime:
                result.append(row[1].replace('#疫情#','')+"\n")
            else:
                print("the time is out",rowtime)
    fr.close()
    save_filename = filepath + starttime + "--" + endtime + ".txt"
    fw = open(save_filename,mode=save_model, encoding='UTF-8')
    fw.writelines(result)
    fw.close()

def removetag(a : str) -> str:
    return a.replace('#疫情#','')

def replacedataname(d: str):
    datafilepath = d + '/DateBase/everymonth/'
    filenamelist = [str(i) for i in range(1, 13)]
    datanamelist = ['%23鐤儏%23.csv', '鏂板啝.csv', '鐤儏.csv']
    resultnamelist = ['疫情tag.csv', '新冠.csv', '疫情.csv']
    for i in filenamelist:
        for j in range(0, 3):
            datapath = datafilepath + i + '/' + datanamelist[j]
            resultpath = datafilepath + i + '/' + resultnamelist[j]
            try:
                os.rename(datapath, resultpath)
            except Exception as e:
                print(e)
                print(f'rename {datapath} fail\r\n')
            else:
                print('rename {} success\r\n'.format(datapath))

def mergedata(MergeFileName:str,MergePath :str,DataPath:str):
    #初始化路径和数据结构
    EffectList = []
    Headers = []
    Merge_path = MergePath + MergeFileName
    #读数据文件
    with open(DataPath, encoding='UTF-8')as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            if (len(Headers) == 0):
                Headers.append(row[0])
                Headers.append(row[1])
                Headers.append(row[2])
            else:
                if(len(row)!=0):
                    EffectList.append(row)
        f.close()
    # 判断文件是否存在,存在则不需要加头
    # path = pathlib.Path("path/file")
    # path.exist()
    if(os.path.exists(Merge_path)):
        Headers.clear()
        print('文件已存在,不需要加表头')
    #写合并的文件
    with open(Merge_path, 'a', encoding='UTF-8-sig')as f:
        f_csv = csv.writer(f)
        if(len(Headers)!=0):
            f_csv.writerow(Headers)
        f_csv.writerows(EffectList)
        f.close()