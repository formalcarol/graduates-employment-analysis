import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

# 讀取資料
df = pd.read_csv('data3-1.csv')

# 計算男女學生未升學就業人數總和
gender_totals = df.groupby('性別')['未升學就業人數'].sum()

# 繪製圓餅圖
plt.figure(figsize=(8, 8))
plt.pie(gender_totals, labels=gender_totals.index, autopct='%1.2f%%', startangle=140)
plt.title('男女學生未升學就業比例')
plt.axis('equal')  # 讓圓餅圖比例相等
plt.savefig('pic2.jpg')