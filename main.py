#coding: utf-8
from tkinter import *
from tkinter import messagebox as tkMessageBox
from tkinter import ttk
import sys
import tkinter
import os
import requests
import shutil

path = "./save"
url = "https://slack.com/api/files.upload"
if not os.path.exists(path):
    os.mkdir(path)

#チャンネル
channel_list = {
    '''
    ここにチャンネル名とチャンネルのIDを連想配列として格納する。
    '''
    }

#拡張子
extend = {
    "txt": ".txt",
    "python": ".py",
    "php": ".php",
    "html": ".html",
    "css": ".css",
    "c": ".c",
    "c++": ".cpp",
    "h": ".h",
    
}

#投稿ボタン機能
def check(event):
    # テキストボックスから入力値を取得
    input_value = EditBox2.get('1.0', 'end -1c')
    comment = EditBox3.get()
    channel = combo.get()
    file_extend = combo_extend.get()
    
    #プルダウンから選択されている物を取得
    if (channel in channel_list.keys()):
        channel_post = channel_list.get(channel)
    if (file_extend in extend.keys()):
        file_extend_post = extend.get(file_extend)
        
    #保存するファイル名を
    fileName = EditBox1.get() + file_extend_post
    title = fileName
    
    data = {
        "token": "user code",　#取得したキーを貼り付ける
        "channels": channel_post,
        "title": title,
        "initial_comment": comment
    }
    #ファイルに書き出し
    path_send = path + "/" + fileName
    f = open(path_send, mode='wt')
    f.write(input_value)
    f.close()
    
    files = {'file': open(path_send, 'rb')}
    requests.post(url, data=data, files=files)
    
    #ファイル削除
    '''
    機能：ファイル数が５つ以上であった場合saveフォルダを初期化する.
    '''
    del_files = os.listdir(path)
    count = len(del_files)
    if count >= 1:
        shutil.rmtree(path)

#画面表示
root = tkinter.Tk()

#ウィンドウ名
root.title("Slack_auto")

#ウィンドウの大きさを設定
root.geometry("550x600")
root.configure(bg="#F5F5F5")

'''
プルダウン
'''
# コンボボックス作成(winに配置, リストの値を読み取り専用に設定)
label1 = tkinter.Label(root, text="投稿チャンネル：", bg="#F5F5F5")
label1.place(x=50, y=0)

combo = ttk.Combobox(root, state="readonly", width=15)
# リストの値を設定
combo["values"] = ("001laravel", "002_vue_js", "01_c", "02_htmlcss",
                   "03_python", "04_php", "05_mysql", "06_jquery", "07_ruby")
combo.pack()

# ファイル形式用プルダウン
label1 = tkinter.Label(root, text="投稿チャンネル：", bg="#F5F5F5")
label1.place(x=50, y=0)
combo_extend = ttk.Combobox(root, state="readonly", width=5)
# ファイル形式設定
combo_extend["values"] = ("txt", "python", "php", "html",
                   "css", "c", "c++", "h")
combo_extend.pack()


#コメント入力欄
label2 = tkinter.Label(root, text="コメント：", bg="#F5F5F5")
label2.place(x=50, y=70)

EditBox3 = tkinter.Entry(width=30)
EditBox3.place(x=150, y=70)

#ファイルのタイトルを入力欄
label3 = tkinter.Label(root, text="タイトル：", bg="#F5F5F5")
label3.place(x=50, y=110)

EditBox1 = tkinter.Entry(width=30)
EditBox1.place(x=150, y=110)

#本文入力欄
label4 = tkinter.Label(root, text="本文", bg="#F5F5F5")
label4.place(x=10, y=150)

EditBox2 = tkinter.Text(root, width=60, height=18, bg="#F5F5F5")
EditBox2.insert(tkinter.END,"")
EditBox2.pack()
EditBox2.place(x=50, y=150)

#ボタン配置
button1 = tkinter.Button(root, text=u'投稿', width=30)
button1.bind("<Button-1>", check)
button1.place(x=130, y=500)

root.mainloop()
