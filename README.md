# cunyu
create on 7/17,2016

- [x] filterEnglishTxt.py
从复合文本中筛选出英文句子。
之后的字幕处理工程还会用到，形成：**数据读取-->提取-->分析-->做总结** 的闭环。
字幕处理之后更新到这里

- [ ] filterEngSrt

- [x] [moviePresaleMonitor.py](https://github.com/QLWeilcf/cunyu/blob/master/moviePresaleMonitor.py)：电影是否开启了预售的监测，如何配置程序定时运行，开电脑自动运行可参考[自动运行脚本 site:jianshu](https://www.jianshu.com/p/ea5cd671b662)。

- [x] text cut and visualize
   -> **WordCloudLCFusing.py**
：文本分词与可视化（词云）一条龙，主打快速实现要求，要调效果就再加入定制参量
包括了：
- 生成词云图，保存词云图到文件，
- 允许词云图个性化。改变背景颜色，改字体，掩膜形状……so on
- 分词，生成词频字典。分词的进阶包括过滤特定词(stop word)，加入限定词
- 整合字幕11111221

- daily anly
  - 字数；
  - 每天字数；
  - 分词；情感分析；
  - 可视化



- 情感分析
readchinaone.py  对中文进行快速分析


- [ ] csvToAllKindsofJson.py 

各种类型的csv转json,后续还会继续补充



