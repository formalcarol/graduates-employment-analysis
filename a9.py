import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

# 讀取資料
df = pd.read_csv('data11-1.csv')

# 按群科別分組，計算每個群科別的未升學就業人數和畢業生人數總和
grouped_by_major = df.groupby('群科別').sum()

# 計算每個群科別的未升學就業人數占畢業生人數的比例
grouped_by_major['未升學就業占比'] = grouped_by_major['未升學就業人數'] / grouped_by_major['畢業生人數']

# 繪製圓餅圖
plt.figure(figsize=(10, 10))

# 繪製圓餅圖，調整標籤位置和百分比位置
plt.pie(grouped_by_major['未升學就業占比'], labels=grouped_by_major.index, autopct='%1.1f%%', startangle=140)

plt.title('不同群科別的未升學就業人數占畢業生人數比例')
plt.axis('equal')  # 使圓餅圖比例相等
plt.savefig('pic9.jpg')
