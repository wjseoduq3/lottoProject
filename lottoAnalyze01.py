import pymysql
import pandas as pd
from collections import Counter  # 빈도수 계산 모듈

import matplotlib.pyplot as plt

dbConn = pymysql.connect(host='192.168.0.100', user='guest01', password='12345', db='lottodbjdy')
sql = 'select * from lottojdy_tbl'
cur = dbConn.cursor()
cur.execute(sql)

dbResult = cur.fetchall()
lotto_df = pd.DataFrame(dbResult, columns=['회차','추첨일','당첨번호1','당첨번호2','당첨번호3',
                                           '당첨번호4','당첨번호5','당첨번호6','보너스번호'])
# print(lotto_df)

lotto_num_df = pd.DataFrame(lotto_df.iloc[:,2:])  # 당첨번호, 보너스번호만 추출하여 데이터프레임화
# print(lotto_num_df)

# print(lotto_num_df.value_counts()) 가독성 안좋음
# print(lotto_num_df['당첨번호1'])
lotto_num_list = list(lotto_num_df['당첨번호1'])+list(lotto_num_df['당첨번호2'])+list(lotto_num_df['당첨번호3'])+list(lotto_num_df['당첨번호4'])+list(lotto_num_df['당첨번호5'])+list(lotto_num_df['당첨번호6'])+list(lotto_num_df['보너스번호'])
# print(len(lotto_num_list))
# print(lotto_num_list)

# 빈도수 찾는 함수 --> module 있음
# for i in range(1, 46):
#     count = 0
#     for num in lotto_num_list:
#         if num == i:
#             count += 1
#     print(f"{i}의 빈도수: {count}")

n_lotto_data = Counter(lotto_num_list)  # 빈도수 계산 모듈 활용
# print(n_lotto_data)

data = pd.Series(n_lotto_data)
data = data.sort_index()
data.plot(figsize=(20,25), kind='barh', grid=True, title='lotto_645')
plt.show()

cur.close()
dbConn.close()
