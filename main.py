import os

import requests
from bs4 import BeautifulSoup
from tkinter import *

# ------------------------------------------------------------------------------------------------------------------

# 컴퓨터정보과 학과공지 url
inhatc_com_sci_notice_url = requests.get("https://cms.itc.ac.kr/site/cs/boardList.do?boardSeq=149&key=485&part=116")
soup = BeautifulSoup(inhatc_com_sci_notice_url.content, "html.parser")

notice_data = soup.select("body > div#wrapper_lightblue > div#wrap_lightblue > div#container > \
                            div#rowgroup1 > div#contents > div#board > form > table.bbs_default_list > \
                            tbody.tb > tr > td.subject > a")

# 학과 공지 제목들 담을 리스트
strArr_notice_data = []

for i in notice_data:
    strArr_notice_data.append(i.get_text())

notice_length = strArr_notice_data.__len__()

root = Tk()
# 제목 지정
root.title("My Useful Window Application")
# 크기 지정
root.geometry("640x480")

# 학과공지 제목 Label
com_sci_notice_label = Label(root, text="학 과 공 지")
com_sci_notice_label.pack()

# 학과공지
notice_area = Text(root, width=100, height=notice_length)
for i in range(notice_length):
    notice_area.insert(END, strArr_notice_data[i] + "\n")
notice_area.pack()

# 버튼 생성
# btn1 = Button(root, text="버튼1", command=btnCmd)
# btn1.grid(row=0, column=0)
# # padx = paddingX, pady = paddingY
# btn2 = Button(root, padx=10, pady=10, text="버튼2", command=change)
# btn2.grid(row=0, column=1)
# # width: 너비, height: 높이
# btn3 = Button(root, width=10, height=10, text="버튼3")
# btn3.grid(row=1, column=0)
# # fg = forground, bg = background
# btn4 = Button(root, fg="green", bg="yellow", text="버튼4")
# btn4.grid(row=1, column=1)

# # Label 생성
# label1 = Label(root, text="안녕하세요~!")
# label1.grid(row=2, column=0)

# # 입력상자 생성
# txt = Text(root, width=30, height=10)
# txt.grid(row=2, column=1)
# txt.insert(END, "글자를 입력하세요.")

# ent = Entry(root, width=30)
# ent.grid(row=3, column=0)

root.mainloop()