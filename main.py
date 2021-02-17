import os
from bs4.element import TemplateString

import requests
from bs4 import BeautifulSoup
from tkinter import *

def load_notice(type):
    # 학과공지 불러오기 버튼 OR 학교공지 불러오기 버튼
    if type == notice_area:
        url = "https://cms.itc.ac.kr/site/cs/boardList.do?boardSeq=149&key=485&part=116"
    else:
        print("학과공지만 가능")
    
    # url을 이용하여 크롤링
    notice_url = requests.get(url)
    soup = BeautifulSoup(notice_url.content, "html.parser")
    notice_data = soup.select("body > div#wrapper_lightblue > div#wrap_lightblue > div#container > \
                                div#rowgroup1 > div#contents > div#board > form > table.bbs_default_list > \
                                tbody.tb > tr > td.subject > a")

    # 학과 공지 제목들 담을 리스트
    strArr_notice_data = []

    for i in notice_data:
        strArr_notice_data.append(i.get_text())

    notice_length = strArr_notice_data.__len__()

    # 읽기,쓰기 모두 가능
    type.configure(state="normal")
    # Text 초기화
    type.delete("1.0", "end")
    # 공지내용 Text 추가
    for i in range(notice_length):
        type.insert(END, strArr_notice_data[i] + "\n")
    # 읽기전용으로 변경
    type.configure(state="disabled")

root = Tk()
# 제목 지정
root.title("My Useful Window Application")
# 크기 지정
root.geometry("640x480")

# 학과공지 제목 Label
com_sci_notice_label = Label(root, text="학 과 공 지")
com_sci_notice_label.pack()

# 학과공지 불러오기 버튼
com_sci_notice_btn = Button(root, text="학과공지 불러오기", command=lambda: load_notice(notice_area))
com_sci_notice_btn.pack()

# 학과공지 state=disabled -> read only
notice_area = Text(root, width=100, height=15)
notice_area.configure(state="disabled")
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