# coding:utf-8
import requests
from bs4 import BeautifulSoup

url = 'http://www.renren.com/974348273/profile'
cookie = 'an_slot=4673; anonymid=k9oz84zw-y358cd; depovince=ZGQT; _r01_=1; taihe_bi_sdk_uid=ee28c0aef212ed48af51c2bce2405a16; taihe_bi_sdk_session=30dd34a0682a744400ac0000f0cc7db1; ick_login=19c2c12c-c122-4d58-8dfa-54cf3eb9cfbf; t=16f4d1b7fe3272909518b8ad091679313; societyguester=16f4d1b7fe3272909518b8ad091679313; id=974348273; xnsid=2ce1fec8; jebecookies=46f3e5ef-65c0-4ef1-8982-96f6e020c612|||||; ver=7.0; loginfrom=null; wp_fold=0; jebe_key=d33c45a2-974b-4f22-8c9b-fe4a94b3e965%7Cf5054a657b5d0f3a6747d91afc7ec499%7C1588384918369%7C1%7C1588384918319'

header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
            , "Cookie": cookie
        }
wbdata = requests.get(url, headers=header)
wbdata.encoding = 'utf-8'
# print(wbdata.text)
with open("csdn.html", "w", encoding="utf-8") as f:
    f.write(wbdata.text);

