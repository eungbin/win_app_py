import os

import requests
from bs4 import BeautifulSoup

inhatc_com_sci_notice_url = requests.get("https://cms.itc.ac.kr/site/cs/boardList.do?boardSeq=149&key=485&part=116")
soup = BeautifulSoup(inhatc_com_sci_notice_url.content, "html.parser")

notice_data = soup.select("body > div#wrapper_lightblue > div#wrap_lightblue > div#container > \
                            div#rowgroup1 > div#contents > div#board > form > table.bbs_default_list > \
                            tbody.tb > tr > td.subject > a")

for i in notice_data:
    print(i.get_text())

os.system("pause")