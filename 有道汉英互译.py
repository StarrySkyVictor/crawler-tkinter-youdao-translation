import requests  
from bs4 import BeautifulSoup  
import urllib.parse  
import tkinter as tk  
from tkinter import messagebox, scrolledtext  

def get_definitions(word):  
    url = f"https://dict.youdao.com/result?word={urllib.parse.quote(word)}&lang=en"   
    headers = {  
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"  
    }  
    
    response = requests.get(url, headers=headers)  
    response.encoding = "utf-8"  
    soup = BeautifulSoup(response.text, "html.parser")  

    # 英语定义部分  
    definition_elements = soup.find_all("span", class_="trans")  
    pos_elements = soup.find_all("span", class_="pos")  

    # 汉译英的部分（假设 HTML 中的类名是这样的，仅供参考，请根据实际情况调整）  
    chinese_translation_elements = soup.find_all("a", class_="point")  
    chinese_pos_elements = soup.find_all("div", class_="word-exp_tran grey")  # 获取所有词性  

    result = ""  # 初始化结果变量  
 
    if definition_elements:  
        definitions = [elem.text.strip() for elem in definition_elements]  
        pos = [pos.text.strip() for pos in pos_elements]  
        for p, d in zip(pos, definitions):  
            result += f'{p}: {d}\n'  
 
    if chinese_translation_elements:  
        chinese_definitions = [elem.text.strip() for elem in chinese_translation_elements]  
        chinese_pos = [pos.text.strip() for pos in chinese_pos_elements]  
        for cp, cd in zip(chinese_pos, chinese_definitions):  
            result += f'{cd}: \n{cp}\n'  
    
    return result.strip()  # 去掉最后的换行  

def query_word():  
    word = entry.get()  
    if word:  
        result = get_definitions(word)  
        output_text.delete(1.0, tk.END)  # 清空输出框  
        output_text.insert(tk.END, result)  # 在输出框中插入结果  
    else:  
        messagebox.showwarning("Input Error", "Please enter a word.")  

# 创建 GUI 界面  
root = tk.Tk()  
root.title("在线翻译")  

label = tk.Label(root, text="输入要翻译的词汇:")  
label.pack(padx=10, pady=10)  

entry = tk.Entry(root, width=50)  
entry.pack(padx=10, pady=10)  

query_button = tk.Button(root, text="翻译", command=query_word)  
query_button.pack(pady=10)  

# 添加一个滚动文本框用于显示结果  
output_text = scrolledtext.ScrolledText(root, width=80, height=20)  
output_text.pack(padx=10, pady=10)  

root.mainloop()