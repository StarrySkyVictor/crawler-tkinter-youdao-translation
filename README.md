# 📘 有道在线翻译小工具

一个基于 **Python + Tkinter + Requests + BeautifulSoup** 的在线翻译桌面程序。  
输入英文或中文单词后，可以调用有道词典网页，爬取释义并显示在 GUI 界面中。  

## ✨ 功能特点
- 支持输入英文单词，返回中文释义、词性、例句等信息  
- 支持输入中文词汇，返回英文释义  
- GUI 界面友好，支持滚动显示长文本  
- 基于 `requests + BeautifulSoup` 实现网页解析  

## 📦 环境依赖
请确保已安装以下依赖：
```bash
python >= 3.8
requests
beautifulsoup4
tkinter   # 通常 Python 自带
