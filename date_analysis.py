from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import time
from collections import Counter
from os import path
import jieba
from snownlp import SnowNLP

jieba.load_userdict(path.join(path.dirname(__file__),'userdict//userdict.txt')) # 导入用户自定义词典
save_wordcloud_file = 'Images/everymonth/'#保存词云位置
word_save_path = "doc/everymonth/词频统计"#保存词频位置
file_save_path = "result/everymonth/merge/"

# 分词处理
def word_segment(text,filename):
    '''
    通过jieba进行分词并通过空格分隔,返回分词后的结果
    '''
    save_path = word_save_path + filename + '.txt'
    # 计算每个词出现的频率，并存入txt文件
    t0 = time.time()
    jieba_word = jieba.cut(text,cut_all=False) # cut_all是分词模式，True是全模式，False是精准模式，默认False
    # 保存词频
    data = []
    for word in jieba_word:
        data.append(word)
    dataDict = Counter(data)
    t1 = time.time()
    print('jieba participle and count operator costs',t1-t0,'s')
    t0 = time.time()
    with open(save_path , 'w' , encoding='UTF-8') as fw:
        for k,v in dataDict.items():
            fw.write("%s,%d\n" % (k,v))
        #  fw.write("%s"%dataDict)
    t1 = time.time()
    print('jieba save word frequecy costs', t1 - t0, 's')
    # 返回分词后的结果
    t0 = time.time()
    jieba_word = jieba.cut(text,cut_all=False) # cut_all是分词模式，True是全模式，False是精准模式，默认False
    seg_list=' '.join(jieba_word)
    t1 = time.time()
    print('jieba return participle operator costs', t1 - t0, 's')
    return seg_list

# 生成词云
def generate_wordcloud(text,filename):
    '''
    输入文本生成词云,如果是中文文本需要先进行分词处理
    '''
    t0 = time.time()
    print('loading the wordcloud setting')
    # 设置显示方式
    d = path.dirname(__file__)
    # mask图片
    # alice_mask = np.array(Image.open(path.join(d, "Images//alice_mask.png")))
    # 中文字体
    font_path = path.join(d ,"font//msyh.ttf")
    # stopwords = set(STOPWORDS)#默认的英语屏蔽词
    stopwords = set(map(str.strip, open('doc//stopwords.txt',encoding='utf-8').readlines()))
    wc = WordCloud(background_color="white",# 设置背景颜色
            max_words=200, # 词云显示的最大词数
            mask=None,#alice_mask,# 设置背景图片
            stopwords=stopwords, # 设置停用词
            font_path=font_path, # 兼容中文字体，不然中文会显示乱码
            scale=2,#按照比例放大画布
                  )

    # 生成词云
    print('generating the wordcloud')
    wc.generate(text)
    t1 = time.time()
    print('generate the wordcloud costs', t1 - t0, 's')
    save_wordcloud = save_wordcloud_file + filename + '.png'
    # 生成的词云图像保存到本地
    wc.to_file(path.join(d, save_wordcloud))


    # 显示图像
    plt.imshow(wc, interpolation='bilinear')
    # interpolation='bilinear' 表示插值方法为双线性插值
    plt.axis("off")# 关掉图像的坐标
    plt.show()

# 获取词云图
def get_wordcloud_pic(filename):
    # 读取文件
    d = path.dirname(__file__)
    filepath = file_save_path + filename + ".txt"
    # text = open(path.join(d, 'doc//十九大报告全文.txt'), encoding='UTF-8').read()
    text = open(path.join(d, filepath), encoding='UTF-8').read()
    # text = open(path.join(d,'doc//alice.txt')).read()

    # 若是中文文本，则先进行分词操作
    print('participle operator is coming')
    text = word_segment(text,filename)

    # 生成词云
    print('generating the wordcloud is coming')
    generate_wordcloud(text,filename)

# 进行情感分析
def emotion_Analysis(filepath: str,filename: str,pic :int = 0) -> float:
    t0 = time.time()
    datapath = filepath + filename + '.txt'
    emo = []
    sum,num = 0,0
    file = open(datapath, mode='r', encoding='UTF-8')
    text = file.read().split()
    for row in text:
        SN = SnowNLP(row)
        emo.append(SN.sentiments)
        sum += SN.sentiments
        num += 1
        if(num % 1000 == 0):
            print(f'{filename}第{num}条数据分析完毕')
    file.close()
    average = sum / num
    t1 = time.time()
    print(f'the emotion analysis costs {t1 - t0} s')
    print(f'{filename} total {num} rows data')
    print(f'the average sentiment of {filename} is', average)
    if(pic == 1):
        x = [str(i) for i in range(1,num+1)]
        generate_Histogram(x,emo,title='try save pic',savepath='Images/histogram/',picname='try_SA')
    return average

# 生成柱状图
def generate_Histogram(x,y,title:str,savepath: str,picname: str):
    plt.style.use("ggplot")
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei'] # plt支持中文
    # 设置常用参数
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.bar(
        x=x,  # Matplotlib自动将非数值变量转化为x轴坐标
        height=y,  # 柱子高度，y轴坐标
        width=0.6,  # 柱子宽度，默认0.8，两根柱子中心的距离默认为1.0
        align="center",  # 柱子的对齐方式，'center' or 'edge'
        color="grey",  # 柱子颜色
        edgecolor="red",  # 柱子边框的颜色
        linewidth=2.0  # 柱子边框线的大小
    )
    ax.set_title(title, fontsize=15)
    # 一个常见的场景是：每根柱子上方添加数值标签
    # 步骤：
    # 1. 准备要添加的标签和坐标
    # 2. 调用ax.annotate()将文本添加到图表
    # 3. 调整样式，例如标签大小，颜色和对齐方式
    xticks = ax.get_xticks()
    for i in range(len(y)):
        xy = (xticks[i], y[i] * 1.03)
        s = str(y[i])
        ax.annotate(
            text=s,  # 要添加的文本
            xy=xy,  # 将文本添加到哪个位置
            fontsize=12,  # 标签大小
            color="blue",  # 标签颜色
            ha="center",  # 水平对齐
            va="baseline"  # 垂直对齐
        )
    save = savepath + picname + '.png'
    plt.savefig(save)
    plt.show()
    return