# WeChat Relay Statistics
# 微信接龙统计程序
微信接龙永远只是一个接龙...没错..一个txt文档<br />
而这个程序则可以将这个~~该死的~~txt文档转换为excel文档<br />
## 示例如下： <br />

![image](https://github.com/tianqo/WeChat-Relay-Statistics/assets/68796895/606e3645-f32d-4e15-a245-e88a58d2f60a)<br />这是微信里的接龙 ~~（时间紧迫直接偷班级群）~~<br />
![image](https://github.com/tianqo/WeChat-Relay-Statistics/assets/68796895/0ba38bdc-9424-4a0f-ae85-270c8e7506fc)<br />而这则是该程序处理后的效果👍👍<br />

**真爽**<br />
## 程序解释：<br />
程序一开始会为你生成一段UUID，请务必放置于接龙备注的最后，这是用于程序识别的UUID，并会在未来开放更多相应功能。<br />
识别完成uuid后会进行对序号的识别（*也就是1. 2. 3.*），***序号是唯一对接龙进行分类的标识符，请勿删除***。<br />
### 关于程序的分类方法
以序号为单位，第一个空格至第二个空格多半为人名，首先提取并放置于excel表格第一列，第二个空格后直接放置于表格第二列，不会做任何分类。<br />
序号与序号之间会有换行，有换行就说明有内容，而这些内容则会以列为单位，依次向后放置（*第二行放置于第三列，第三行放置于第四列...依此类推*）。<br />
## 使用方法： <br />
### 环境 <br />
### requirement <br />
    python 3.12
    openpyxl
### 执行： <br />
确保自己已经完全下载了本代码并且进入了code文件夹环境，然后使用cmd执行以下代码：<br />
```
python logic.py
```
但由于一些不可抗力的因素，我推荐还是使用如下方法：<br />
![image](https://github.com/tianqo/WeChat-Relay-Statistics/assets/68796895/24ffae61-2b03-4bb4-bf60-99824a4c0475)<br />
使用idle打开logic.py文件并执行（没错这样更方便）<br />
![image](https://github.com/tianqo/WeChat-Relay-Statistics/assets/68796895/fda7037b-e60a-4a65-b097-96175dd700a5)<br />
出现以上提示多半就是执行成功了<br />
## 操作注意事项
出于某些原因，接龙的序号与序号之间必须有个换行<br />
![image](https://github.com/tianqo/WeChat-Relay-Statistics/assets/68796895/58840b65-e21c-423d-b5dd-2acfb8da0a06)这样不行<br />
![image](https://github.com/tianqo/WeChat-Relay-Statistics/assets/68796895/c2aac2ef-08fb-4396-85e9-2510dd4cdc37)必须这样<br />
***如果不换行会导致程序卡入死循环，暂时没找到解决办法***<br />
## 关于开放的端口：<br />
使用本程序的人肯定会发现程序的uuid其实并没有什么实质性的作用，甚至删除关于uuid的所有代码都不会对程序有任何影响。那是因为在控制台界面，其实并不好做对uuid的分类，反观如果是程序化界面，我们（用户）可以对uuid进行更多的花样性设置（这次接龙的主要目的、用途、时间、日期......），而在控制台上就会显得非常困难，*毕竟谁也不想对着依托乌漆嘛黑的界面敲一顿代码来设置一些没啥用的东西*，而我正好不会写程序化界面，所以只好将这个功能暂时晾置在这里，等待以后的开发。<br />
**简单来说就是uuid是为在未来进行客制化自定义而设计的标识符，~~现在还不知道怎么做~~**

