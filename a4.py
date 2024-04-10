import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

# 讀取資料
df = pd.read_csv('data7-1.csv')

# 按縣市分組，計算每個縣市的未升學就業人數總和
grouped_by_location = df.groupby('學校所在地別').sum()
grouped_by_location['未升學就業占比'] = grouped_by_location['未升學就業人數'] / grouped_by_location['畢業生人數']

# 繪製圓餅圖
plt.figure(figsize=(10, 8))
unemployed_ratio = grouped_by_location['未升學就業占比'].values
locations = grouped_by_location.index
# 繪製圓餅圖，調整標籤位置和百分比位置
plt.pie(unemployed_ratio, labels=locations, autopct='%1.2f%%', startangle=125)

plt.title('縣市未升學就業占比分佈 = 未升學就業/畢業生人數')
plt.axis('equal')  # 使圓餅圖比例相等
plt.savefig('pic4.png')