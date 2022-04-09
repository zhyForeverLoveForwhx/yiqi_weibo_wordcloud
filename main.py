# This is a sample python to get some weibo msg
import os
import time

import File_opration as FOP
import date_analysis as DAS
from os import path

def Main():
    #处理原始文件
    d = path.dirname(__file__)
    # FOP.replacedataname(d)

    #处理初始数据
    # datafilepath    = d + '/DateBase/everymonth/'
    resultfilepath  = d + '/result/everymonth/'
    filenamelist    = [str(i) for i in range(1, 13)]
    # datanamelist    = ['疫情tag', '新冠', '疫情']
    # for i in filenamelist:
    #     datapath        = datafilepath + i + '/'
    #     resultpath      = resultfilepath + i + '/'
    #     for j in range(0, 3):
    #         try:
    #             FOP.save_result(Filename=datanamelist[j],resultpath=resultpath,datapath=datapath)
    #         except Exception as e:
    #             print(e)
    #             print(f'make {datapath+datanamelist[j]} fail\r\n')
    #         else:
    #             print('make {} success\r\n'.format(datapath+datanamelist[j]))
    print('going on')
    #合并数据
    # ResultDataList = ['疫情tag_result.csv', '新冠_result.csv', '疫情_result.csv']
    mergefilepath = d + '/' + 'result/everymonth/merge/'
    mergefilename = 'MergeEveryMonth.csv'
    # for j in filenamelist:
    #     for i in ResultDataList:
    #         resultdata = resultfilepath + j + '/' + i
    #         if(os.path.exists(resultdata)):
    #             try:
    #                 FOP.mergedata(MergeFileName=mergefilename,MergePath=mergefilepath,DataPath=resultdata)
    #             except Exception as e:
    #                 print(e)
    #                 print('the merging data is failed')
    #             else:
    #                 print(f'the merging data {resultdata} is successful')
    #         else:
    #             print('the {} is not exist'.format(resultdata))

    #按时间分类数据
    starttimelist=["2020-01-01","2020-02-01","2020-03-01","2020-04-01","2020-05-01","2020-06-01",\
                   "2020-07-01","2020-08-01","2020-09-01","2020-10-01","2020-11-01","2020-12-01"]
    endtimelist  =["2020-02-02","2020-03-02","2020-04-02","2020-05-01","2020-06-01","2020-07-01",\
                   "2020-08-02","2020-09-02","2020-10-02","2020-11-02","2020-12-02","2021-01-02"]
    # 一整年
    # FOP.gettxt(filepath=mergefilepath, filename=mergefilename, \
    #                        starttime=starttimelist[0], endtime=endtimelist[-1])
    # 十二个月
    # for i in range(0,12):
    #     try:
    #         FOP.gettxt(filepath=mergefilepath,filename=mergefilename,\
    #                    starttime=starttimelist[i], endtime=endtimelist[i])
    #     except Exception as e:
    #         print(e)
    #         print(f'classification the month {i+1} is failed')
    #     else:
    #         print(f'classification the month {i+1} is successful')

    # 生成词云可视化图像
    # for i in range(0,12):
    #     file_name = starttimelist[i] + '--' + endtimelist[i]
    #     t0 = time.time()
    #     try:
    #         DAS.get_wordcloud_pic(filename=file_name)
    #     except Exception as e:
    #         print(e)
    #     else:
    #         print('successful')
    #     t1 = time.time()
    #     print(f'the {file_name}total generate wordcloud operator costs', t1 - t0, 's')
    try:
        emo = DAS.emotion_Analysis( d + '/result/','try_SA')
    except Exception as e:
        print(e)
        print('failed')
    else:
        print('the emotion Analysis successful')
        print('the average emotion is ',emo)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    Main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
