---
title: "WeChat Relay Statistics"
author: "tianqo"
date: "2024-08-06"
output:
  pdf_document:
    latex_engine: xeHarmoHarmo
    mainfont: Harmony SC sans  # 指定主字体为鸿蒙
---

# WeChat Relay Statistics
# 微信接龙统计程序
微信接龙永远只是一个接龙...没错..一个txt文档

而这个程序则可以将这个~~该死的~~txt文档转换为excel文档

## 示例如下： 


![image](https://github.com/tianqo/WeChat-Relay-Statistics/assets/68796895/606e3645-f32d-4e15-a245-e88a58d2f60a)

这是微信里的接龙
~~（时间紧任务重 直接偷班级群）~~

![image](https://github.com/tianqo/WeChat-Relay-Statistics/assets/68796895/0ba38bdc-9424-4a0f-ae85-270c8e7506fc)<br />而这则是该程序处理后的效果👍👍

**真爽**

---

## 程序说明（**必看**）：

*对于**统计**这一词的问题，我也有做过了解，目前的程序的确只是实现了归类管理的功能，可能有人会认为这是一个分类程序，并且其他程序更加完善并且操作丰富。而实际上归类管理也是属于统计的一部分，程序并没有跑题，而且市面上更没有所谓的更加完美的能实现我目前的**分类**程序。*

*综上，该程序是**独一无二**并且**完美符合要求**的统计程序，而那些人理解的统计事实上才是已经拥有的程序（统计次数、出现频率、总计等），所以本程序强调的是杂乱项的统计管理，而不是对次数的统计计数，这需要搞清楚。*

*所以说这个程序的真正操作是**对文本内容进行分类合并，再使用excel或者only office等程序对文件进行进一步统计**。*

*对于实在无法理解**统计**一词的人我也实在没办法，只好继续开发二次统计的程序。*

---

## 程序解释：

程序正式运行时会列举出所有你存放在txt-collection文件夹下的txt文件，然后让你选择一个文件进行归类。

### 关于程序的分类方法

以序号为单位，第一个空格至第二个空格多半为人名，首先提取并放置于excel表格第一列，第二个空格后放置于表格第二列,依次类推。


---

## 使用方法： 

### 环境 

### requirement 

```
  et-xmlfile==1.1.0
  jieba==0.42.1
  numpy==2.0.1
  openpyxl==3.1.5
  pandas==2.2.2
  prettytable==3.10.2
  python-dateutil==2.9.0.post0
  pytz==2024.1
  six==1.16.0
  tzdata==2024.1
  wcwidth==0.2.13
```

### 执行：

将你复制下来的接龙黏贴到txt文档里，放进txt-collection文件夹里。

文件夹允许同时存在多个接龙文档，命名随意，支持中文。

使用python执行runme.py即可，程序将会引导你执行每一步操作。

a选项将执行归类操作，也就是开头图片呈现的操作，他将为你的接龙文件进行excel表格的生成。

b选项将执行统计操作，但只能进行对出现次数的统计，它将为你的接龙文件进行excel表格的统计。

**所有程序的执行都必须先经过a程序以后再进行下一个程序执行**

---

### 一些建议：

程序运行于python环境下，你可以使用pycharm或者vscode等IDE进行开发，也可以使用python自带的IDLE进行运行。

但是注意：**pycharm和vscode的路径管理模式不同，pycharm是以运行的程序为基准进行目录的构建，而vscode则是以打开的文件夹为基准构建**。

如果不理解也没关系，目前的文件排序方式应该是解决了这个问题。你只需**继续按照原步骤直接运行runme.py即可**。

如果实在有问题就去issue区找，或者直接联系我。

---




