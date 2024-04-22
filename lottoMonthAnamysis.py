import pymysql
import pandas as pd
from collections import Counter  # 빈도수 계산 모듈
from datetime import datetime

import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

dbConn = pymysql.connect(host='192.168.0.100', user='guest01', password='12345', db='lottodbjdy')
sql = 'select * from lottojdy_tbl'
cur = dbConn.cursor()
cur.execute(sql)

dbResult = cur.fetchall()

lotto_df = pd.DataFrame(dbResult, columns=['회차','추첨일','당첨번호1','당첨번호2','당첨번호3',
                                           '당첨번호4','당첨번호5','당첨번호6','보너스번호'])
# print(lotto_df)

lotto_df['추첨일'] = pd.to_datetime(lotto_df['추첨일'])  # Pandas 날짜형식으로 변환
# 월만 추출하여 새로운 필드 생성
lotto_df['추첨월'] = lotto_df['추첨일'].dt.month
# print(lotto_df)

# 1월로 연습
# lotto_month_01 = lotto_df[lotto_df['추첨월'] == 1]
# # print(lotto_month_01)
#
# month_01_lottoList = list(lotto_month_01['당첨번호1'])+list(lotto_month_01['당첨번호2'])+list(lotto_month_01['당첨번호3'])+list(lotto_month_01['당첨번호4'])+list(lotto_month_01['당첨번호5'])+list(lotto_month_01['당첨번호6'])+list(lotto_month_01['보너스번호'])
#
# n_lotto_data = Counter(month_01_lottoList)  # 빈도수 계산 모듈 활용
# # print(n_lotto_data)
#
# data = pd.Series(n_lotto_data)
# data = data.sort_index()
# data.plot(figsize=(20,25), kind='barh', grid=True, title='1월의 lotto_645 빈도수')

for month in range(1, 13):
    lotto_month_df = lotto_df[lotto_df['추첨월'] == month]
    month_lottoList = (list(lotto_month_df['당첨번호1']) + list(lotto_month_df['당첨번호2']) +
                          list(lotto_month_df['당첨번호3']) + list(lotto_month_df['당첨번호4']) +
                          list(lotto_month_df['당첨번호5']) + list(lotto_month_df['당첨번호6']) + list(lotto_month_df['보너스번호']))
    month_freq =Counter(month_lottoList)  # 월별 출현 로또번호 빈도수
    data = pd.Series(month_freq)
    sorted_data = data.sort_values(ascending=False)
    top10_data = sorted_data.head(10)

    plt.subplot(4, 3, month)
    plt.subplots_adjust(left=0.125, bottom=0.1, top=0.9, wspace=0.3, hspace=0.5)

    top10_data.plot(figsize=(10, 20), kind='barh', grid=True) #title='월별 로또번호 빈출 10선')
    plt.title(f"{month}월 최다 출현 번호")
    plt.xlabel('빈도수')
    plt.ylabel('로또번호')

plt.show()

cur.close()
dbConn.close()
