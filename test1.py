import csv
import pandas as pd

#header      = [id,bid,user_id,用户昵称,微博正文,头条文章url,发布位置,艾特用户,话题,转发数,评论数,点赞数,发布时间,发布工具,微博图片url,微博视频url,retweet_id]
File_Path   = "D:\python_py\weibo_spider\weibo-search\结果文件\%23疫情%23"
Filename    = "%23疫情%23"
CSV_Path    = File_Path+"\\"+Filename+".csv"
Result_Path = Filename + "_result" + ".csv"
EffectList  = []
Headers     = []

# data = pd.read_csv(CSV_Path)
# print(data)

with open(CSV_Path, encoding='UTF-8')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        if(len(Headers) == 0):
            Headers.append(row[1])
            Headers.append(row[4])
            Headers.append(row[12])
        else:
            EffectList.append([row[1],row[4],row[12]])


print(Headers)
print(EffectList)

with open(Result_Path,'w', encoding='UTF-8-sig')as f:
    f_csv = csv.writer(f)
    f_csv.writerow(Headers)
    f_csv.writerows(EffectList)