---
title: "WeChat Relay Statistics"
author: "tianqo"
date: "2024-08-06"
output:
  pdf_document:
    latex_engine: xelatex
    mainfont: SimSun  # 指定主字体为宋体
    sansfont: SimHei  # 指定无衬线字体为黑体
    monofont: "Courier New"  # 指定等宽字体
    CJKoptions: BoldFont=SimHei, ItalicFont=KaiTi  # 指定CJK字体的加粗和斜体
---

# WeChat Relay Statistics
# 微信接龙统计程序
微信接龙永远只是一个接龙...没错..一个txt文档<br />
而这个程序则可以将这个~~该死的~~txt文档转换为excel文档<br />
## 示例如下： <br />

![image](https://github.com/tianqo/WeChat-Relay-Statistics/assets/68796895/606e3645-f32d-4e15-a245-e88a58d2f60a)<br />这是微信里的接龙 ~~（时间紧迫直接偷班级群）~~<br />
![image](https://github.com/tianqo/WeChat-Relay-Statistics/assets/68796895/0ba38bdc-9424-4a0f-ae85-270c8e7506fc)<br />而这则是该程序处理后的效果👍👍<br />

**真爽**<br />

---

## 程序说明（**必看**）：

*对于**统计**这一词的问题，我也有做过了解，目前的程序的确只是实现了归类管理的功能，可能有人会认为这是一个分类程序，并且其他程序更加完善并且操作丰富。而实际上归类管理也是属于统计的一部分，程序并没有跑题，而且市面上更没有所谓的更加完美的能实现我目前的**分类**程序。*

*综上，该程序是**独一无二**并且**完美符合要求**的统计程序，而那些人理解的统计事实上才是已经拥有的程序（统计次数、出现频率、总计等），所以本程序强调的是杂乱项的统计管理，而不是对次数的统计计数，这需要搞清楚。*

*所以说这个程序的真正操作是**对文本内容进行分类合并，再使用excel或者only office等程序对文件进行进一步统计**。*

*对于实在无法理解**统计**一词的人我也实在没办法，只好继续开发二次统计的程序。*

---

## 程序解释：<br />
程序一开始会为你生成一段UUID，请务必放置于接龙备注的最后，这是用于程序识别的UUID，并会在未来开放更多相应功能。<br />
识别完成uuid后会进行对序号的识别（*也就是1. 2. 3.*），***序号是唯一对接龙进行分类的标识符，请勿删除***。<br />
### 关于程序的分类方法
以序号为单位，第一个空格至第二个空格多半为人名，首先提取并放置于excel表格第一列，第二个空格后直接放置于表格第二列，不会做任何分类。<br />
序号与序号之间会有换行，有换行就说明有内容，而这些内容则会以列为单位，依次向后放置（*第二行放置于第三列，第三行放置于第四列...依此类推*）。

---

## 使用方法： <br />
### 环境 <br />
### requirement <br />
    openpyxl
### 执行： <br />
确保自己已经完全下载了本代码并且进入了文件夹根目录，然后使用cmd执行以下代码：<br />
```
python logic.py
```
但我推荐还是使用如下方法：<br />
![image](https://github.com/tianqo/WeChat-Relay-Statistics/assets/68796895/24ffae61-2b03-4bb4-bf60-99824a4c0475)<br />
使用idle打开logic.py文件并执行（没错这样更方便）<br />
![image](https://github.com/tianqo/WeChat-Relay-Statistics/assets/68796895/fda7037b-e60a-4a65-b097-96175dd700a5)<br />
出现以上提示多半就是执行成功了<br />
## 操作注意事项
出于某些原因，接龙的序号与序号之间必须有个换行<br />
![image](https://github.com/tianqo/WeChat-Relay-Statistics/assets/68796895/58840b65-e21c-423d-b5dd-2acfb8da0a06)这样不行<br />
![image](https://github.com/tianqo/WeChat-Relay-Statistics/assets/68796895/c2aac2ef-08fb-4396-85e9-2510dd4cdc37)必须这样<br />
***如果不换行会导致程序卡入死循环，暂时没找到解决办法***

---

## 关于开放的端口：<br />
使用本程序的人肯定会发现程序的uuid其实并没有什么实质性的作用，甚至删除关于uuid的所有代码都不会对程序有任何影响。那是因为在控制台界面，其实并不好做对uuid的分类，反观如果是程序化界面，我们（用户）可以对uuid进行更多的花样性设置（这次接龙的主要目的、用途、时间、日期......），而在控制台上就会显得非常困难，*毕竟谁也不想对着依托乌漆嘛黑的界面敲一顿代码来设置一些没啥用的东西*，而我正好不会写程序化界面，所以只好将这个功能暂时晾置在这里，等待以后的开发。<br />
**简单来说就是uuid是为在未来进行客制化自定义而设计的标识符，~~现在还不知道怎么做~~**

