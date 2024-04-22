import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd


def get_lottoNumber(count):  # count: 추첨회차 입력
    url = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={count}"
    html = requests.get(url).text
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')
    date = soup.find('p', {'class': 'desc'}).text
    lottoDate = datetime.strptime(date, "(%Y년 %m월 %d일 추첨)")
    # print(date)
    # print(lottoDate)
    lottoNumber = soup.find('div', {'class': 'num win'}).find('p').text.strip().split('\n')
    lottoNumberList = []
    for num in lottoNumber:
        lottoNumberList.append(int(num))
    # print(lottoNumber)
    # print(lottoNumberList)
    bonusNumber = int(soup.find('div', {'class': 'num bonus'}).find('p').text.strip())
    # print(bonusNumber)
    lottoDic = {'lottoDate': lottoDate, 'lottoNumber': lottoNumberList, 'bonusNumber': bonusNumber}
    return lottoDic

lottoDf_list = []

for count in range(1, 1117):
    lottoResult = get_lottoNumber(count)
    lottoDf_list.append({
        'count': count,  # 회차
        'lottoDate': lottoResult['lottoDate'],  # 추첨일
        'lottoNum1': lottoResult['lottoNumber'][0],
        'lottoNum2': lottoResult['lottoNumber'][1],
        'lottoNum3': lottoResult['lottoNumber'][2],
        'lottoNum4': lottoResult['lottoNumber'][3],
        'lottoNum5': lottoResult['lottoNumber'][4],
        'lottoNum6': lottoResult['lottoNumber'][5],
        'bonusNum': lottoResult['bonusNumber']
    })
    print(f"{count}회 처리중...")
# print(lottoDf_list)

lottoDF = pd.DataFrame(data=lottoDf_list, columns=['count','lottoDate',
                            'lottoNum1','lottoNum2','lottoNum3','lottoNum4','lottoNum5',
                            'lottoNum6','bonusNum'])
print(lottoDF)








