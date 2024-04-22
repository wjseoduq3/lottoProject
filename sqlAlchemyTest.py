from sqlalchemy import create_engine
import pandas as pd
import pymysql

data = {'학번': range(2000, 2015), '성적':[70, 60, 90, 100, 56, 63, 85, 88, 75, 99, 100,100,100,100,100]}
# 기존 테이블에 신규 데이터 추가까지 가능
df = pd.DataFrame(data=data, columns=['학번', '성적'])
print(df)

engine = create_engine('mysql+pymysql://guest01:12345@192.168.0.100:3306/lottodbjdy?charset=utf8mb4')
engine.connect()

df.to_sql(name='test_tbl',con=engine,if_exists='append',index=False)