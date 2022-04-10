from snownlp import sentiment

if __name__ == "__main__":
  # 重新训练模型
  sentiment.train('train/neg.txt', 'train/pos.txt')
  # 保存好新训练的模型
  sentiment.save('train/model/sentiment.marshal')