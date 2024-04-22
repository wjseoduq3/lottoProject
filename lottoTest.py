import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=1116"

html = requests.get(url).text

# print(html)

soup = BeautifulSoup(html, 'html.parser')

date = soup.find('p', {'class' : 'desc'}).text
lottoDate = datetime.strptime(date, "(%Y년 %m월 %d일 추첨)")
# print(date)
print(lottoDate)



# print(date)

lottoNumber = soup.find('div', {'class' : 'num win'}).find('p').text.strip().split('\n')
lottoNumberList = []
for num in lottoNumber:
    lottoNumberList.append(int(num))

# print(lottoNumber)
print(lottoNumberList)

bonusNumber = int(soup.find('div', {'class' : 'num bonus'}).find('p').text.strip())
print(bonusNumber)

