from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

from collections import Counter
from os import path
import jieba

jieba.load_userdict(path.join(path.dirname(__file__),'userdict//userdict.txt')) # 导入用户自定义词典
save_wordcloud_file = 'Images//everymonth//'#保存词云位置
word_save_path = "doc//everymonth//词频统计"#保存词频位置
file_save_path = "result//everymonth//"

def word_segment(text,filename):
    '''
    通过jieba进行分词并通过空格分隔,返回分词后的结果
    '''
    save_path = word_save_path + filename + '.txt'
    # 计算每个词出现的频率，并存入txt文件
    jieba_word=jieba.cut(text,cut_all=False) # cut_all是分词模式，True是全模式，False是精准模式，默认False
    data = []
    for word in jieba_word:
        data.append(word)
    dataDict = Counter(data)
    with open(save_path , 'w' , encoding='UTF-8') as fw:
        for k,v in dataDict.items():
            fw.write("%s,%d\n" % (k,v))
        #  fw.write("%s"%dataDict)
    # 返回分词后的结果
    jieba_word=jieba.cut(text,cut_all=False) # cut_all是分词模式，True是全模式，False是精准模式，默认False
    seg_list=' '.join(jieba_word)
    return seg_list

def generate_wordcloud(text,filename):
    '''
    输入文本生成词云,如果是中文文本需要先进行分词处理
    '''
    # 设置显示方式
    d = path.dirname(__file__)
    # mask图片
    # alice_mask = np.array(Image.open(path.join(d, "Images//alice_mask.png")))
    # 中文字体
    font_path = path.join(d ,"font//msyh.ttf")
    # stopwords = set(STOPWORDS)#默认的英语屏蔽词
    stopwords = set(map(str.strip, open('doc//stopwords.txt',encoding='utf-8').readlines()))
    wc = WordCloud(background_color="white",# 设置背景颜色
            max_words=100, # 词云显示的最大词数
            mask=None,#alice_mask,# 设置背景图片
            stopwords=stopwords, # 设置停用词
            font_path=font_path, # 兼容中文字体，不然中文会显示乱码
            scale=2,#按照比例放大画布
                  )

    # 生成词云
    wc.generate(text)
    save_wordcloud = save_wordcloud_file + filename + '.png'
    # 生成的词云图像保存到本地
    wc.to_file(path.join(d, save_wordcloud))

    # 显示图像
    plt.imshow(wc, interpolation='bilinear')
    # interpolation='bilinear' 表示插值方法为双线性插值
    plt.axis("off")# 关掉图像的坐标
    plt.show()

def get_wordcloud_pic(filename):
    # 读取文件
    d = path.dirname(__file__)
    filepath = file_save_path + filename + ".txt"
    # text = open(path.join(d, 'doc//十九大报告全文.txt'), encoding='UTF-8').read()
    text = open(path.join(d, filepath), encoding='UTF-8').read()
    # text = open(path.join(d,'doc//alice.txt')).read()

    # 若是中文文本，则先进行分词操作
    text = word_segment(text,filename)

    # 生成词云
    generate_wordcloud(text,filename)