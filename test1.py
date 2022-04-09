#柱状图的试验
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from os import path
import time

# %matplotlib inline
# n=list(map(int,input().strip('[]').split(',')))
# n = [int(i) for i in n]

# datapath = 'result/try_SA.txt'
# emo = []
# # sum,num = 0
# file = open(datapath, mode='r', encoding='UTF-8')
# text = file.read().split('\n')
# print(text)


plt.style.use("ggplot")

# # 虚拟数据
# x = ["A", "B", "C", "D", "E", "F", "G", "H"]
# y = [150, 85.2, 65.2, 85, 45, 120, 51, 64]

# 柱状图和散点图不同，散点图的(x,y)均为数值变量
# 柱状图的x轴显示分类变量，有两种处理方式
# 方式1：自己创建x轴坐标，并提供对应的标签
# 方式2：让Matplotlib自动完成映射

# 方式1
# xticks = np.arange(len(x))  # 每根柱子的x轴坐标
# xlabels = x  # 每根柱子的标签
# fig, ax = plt.subplots(figsize=(10, 7))
# ax.bar(x=xticks, height=y, tick_label=xlabels)

# 方式2（推荐）
# fig, ax = plt.subplots(figsize=(10, 7))
# ax.bar(x=x, height=y)
# ax.set_title("Simple Bar Plot", fontsize=15)

# 设置常用参数
# fig, ax = plt.subplots(figsize=(10, 7))
# ax.bar(
#     x=x,  # Matplotlib自动将非数值变量转化为x轴坐标
#     height=y,  # 柱子高度，y轴坐标
#     width=0.6,  # 柱子宽度，默认0.8，两根柱子中心的距离默认为1.0
#     align="center",  # 柱子的对齐方式，'center' or 'edge'
#     color="grey",  # 柱子颜色
#     edgecolor="red",  # 柱子边框的颜色
#     linewidth=2.0  # 柱子边框线的大小
# )
# ax.set_title("Adjust Styles of Bar plot", fontsize=15)

# 一个常见的场景是：每根柱子上方添加数值标签
# 步骤：
# 1. 准备要添加的标签和坐标
# 2. 调用ax.annotate()将文本添加到图表
# 3. 调整样式，例如标签大小，颜色和对齐方式
# xticks = ax.get_xticks()
# for i in range(len(y)):
#     xy = (xticks[i], y[i] * 1.03)
#     s = str(y[i])
#     ax.annotate(
#         text=s,  # 要添加的文本
#         xy=xy,  # 将文本添加到哪个位置
#         fontsize=12,  # 标签大小
#         color="blue",  # 标签颜色
#         ha="center",  # 水平对齐
#         va="baseline"  # 垂直对齐
#     )


#data

shops = ["A", "B", "C", "D", "E", "F"]
sales_product_1 = [100, 85, 56, 42, 72, 15]
sales_product_2 = [50, 120, 65, 85, 25, 55]
sales_product_3 = [20, 35, 45, 27, 55, 65]

# 创建分组柱状图，需要自己控制x轴坐标
xticks = np.arange(len(shops))

fig, ax = plt.subplots(figsize=(10, 7))
# 所有门店第一种产品的销量，注意控制柱子的宽度，这里选择0.25
ax.bar(xticks, sales_product_1, width=0.25, label="Product_1", color="red")
# 所有门店第二种产品的销量，通过微调x轴坐标来调整新增柱子的位置
ax.bar(xticks + 0.25, sales_product_2, width=0.25, label="Product_2", color="blue")
# 所有门店第三种产品的销量，继续微调x轴坐标调整新增柱子的位置
ax.bar(xticks + 0.5, sales_product_3, width=0.25, label="Product_3", color="green")

ax.set_title("Grouped Bar plot", fontsize=15)
ax.set_xlabel("Shops")
ax.set_ylabel("Product Sales")
ax.legend()

# 最后调整x轴标签的位置
ax.set_xticks(xticks + 0.25)
ax.set_xticklabels(shops)

plt.show()

