# Python - NLTK

## 简介

1. 在自然语言处理(NLP)中，我们常用的库就是NLTK
2. 目的在于开发可以理解人类语言的应用程序和服务

## 实现

* 搜索引擎
* 社交网站的推送
* 语音引擎(siri)
* 垃圾邮件过滤(机器学习的范畴)

## 安装

1. 本人之前安装过anaconda内置有NLTK库，但是可以采用`pip`等方式安装

2. ```python
   import nltk
   # 首次安装需要nltk扩展包,建议安装所有
   nltk.download()
   ```

## Python Tokenize

```python
# 首先抓一个网页
import urllib.request
response = urllib.request.urlopen('http://php.net/')
html = response.read()
# 对网页的文本进行过滤，抽取出文本并规格化
from bs4 import BeautifulSoup
soup = BeautifulSoup(html , 'lxml')
text = soup.get_text(strip = True)
# print(text)      # 结果是一个长字符串
# 将文本按照单词分开成列表
tokens = text.split()
# print(tokens)
# 统计词频
import nltk
freq = nltk.FreqDist(tokens)
for key , value in freq.items():
    print(key , ':' , value)
freq.plot()    # 打印次品统计结果，需要matplotlib的支持
# 如果我们的打印的结果非常的糟糕，可以限定打印的前几名
freq.plot(20)    # 打印前20
```

![wordfreq](/home/lantian/File/Software-Engine/Sources/Python-NLTK-Simple/wordfreq.png)

1. 需要注意的是，我们的of , a  ,an都是没有意义的停用词，停用词一般都需要过滤掉f防止影响我们的分析结果

2. NLTK自带有停用词列表，可以获取不同的语言的停用词

3. 获取停用词

   ```python
   from nltk.corpus import stopwords    # corpus是我们的第三方的nltk扩展包
   stopwords.words('english')    # 英文停用词,以列表的形式返回

   # 对上述的数据进行清洗
   clean_tokens = []
   sr = stopwords.words('english')
   for token in tokens:
       if token not in sr:
           clean_tokens.append(token)
   freq = nltk.FreqDist(clean_tokens)
   for key , value in freq.items():    # 清洗后数据
       print(key , ':' , value)

   freq.plot(20)
   ```

![nostopwordswordfreq](/home/lantian/File/Software-Engine/Sources/Python-NLTK-Simple/nostopwordswordfreq.png)

## NLTK Tokenize

所谓的token:

1. 句子分割成词，段落分割成句子的支持
2. NLTK自带的分割支持是经过训练和并且可以是适应多种语言的(内置使用的punkt模块)

```python
t = 'hello adam. how are you ? i hope everything is going well.today is a good day,see you dude.'
from nltk.tokenize import sent_tokenize    # 将句子分割成单词的模块
print(sent_tokenize(t))    # 对句子进行分割
```

**多语言的分割**

```python
from nltk.tokenize import sent_tokenize
sent_tokenize(string , 'french')    # French / Chinese / English ...	
```

**同义词处理**

1. 第三方库`wordnet`

2. 这个第三方库包含同义词组和简短的定义

   ```python
   from nltk.corpus import wordnet
   syn = wordnet.synsets('pain')
   print(syn[0].definition() , syn[0].examples())
   ```


3. 获取同义词

   ```python
   from nltk.corpus import wordnet
   synonyms = []
   for syn in wordnet.synsets('computer'):
       for lemma in syn.lemmas():
           synonyms.append(lemma.name())    # 同义词具有name属性，可以打印该同义词
   print(synonyms)
   ```

4. 获取反义词

   ```python
   from nltk.corpus import wordnet
   antoyms = []
   for syn in wordnet.synsets('small'):
       for l in syn.lemmas():
           if l.antoyms():    # 如果small的同义词有反义词，添加
               antonyms.append(l.antoyms()[0].name())
   print(antoyms)
   ```

**词干提取**

1. 词干提取是去除词缀得到词根的过程，例如将working转化work

2. 常见的是波特词干算法 / Lancaster词干算法

   ```python
   from nltk.stem import PorterStemmer
   stemmer = PorterStemmer()
   print(stemmer.stem('working'))
   print(stemmer.stem('worked'))
   ```

3. 非英文词干提取

   `SnowballStemmer`支持13种语言的词干提取

   1. 显示支持的语言

      ```python
      from nltk.stem import SnowballStemmer
      print(SnowballStemmer.languages)

      '''
      ('danish', 'dutch', 'english', 'finnish', 'french', 'german', 'hungarian', 'italian', 'norwegian', 'porter', 'portuguese', 'romanian', 'russian', 'spanish', 'swedish')
      '''
      ```

   2. 提取

      ```python
      from nltk.stem import SnowballStemmer
      french_stemmer = SnowballStemmer('french')
      print(french_stemmer.stem('french word'))
      ```

4. 单词变体还原

   有时候磁感提取的结果是错误的，我们需要使用单词的变体还原的策略

   ```python
   # 对比我们的词干提取的结果
   from nltk.stem import WordNetLemmatizer
   lemmatizer = WordNetLemmatizer()
   print(lemmatizer.lemmatize('increases'))
   ```

   1. 结果可能会是一个同义词

   2. 但是总是得到相同的次

   3. 指定得到的变体还原单词的词义是动词还是名词

      ```python
      # v - 动词
      # n - 名词
      # a - 形容词
      # r - 副词
      lemmatizer.lemmatize('playing' , pos = 'v')
      lemmatizer.lemmatize('playing' , pos = 'n')
      lemmatizer.lemmatize('playing' , pos = 'a')
      lemmatizer.lemmatize('playing' , pos = 'r')
      ```

5. 词干变体还原和单词的词干提取的区别

   1. 词干提取速度快，准确度低
   2. 变体还原的速度不慢，准确度高，而且允许我们返还的单词可以使同义词，更有扩展性