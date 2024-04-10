import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

# 讀取資料
df = pd.read_csv('data11-1.csv')

# 按群科別分組，計算每個群科別的畢業生人數總和
grouped_by_major = df.groupby('群科別')['畢業生人數'].sum().sort_values()

# 繪製圓餅圖
plt.figure(figsize=(10, 10))

# 繪製圓餅圖，調整標籤位置和百分比位置
plt.pie(grouped_by_major, labels=grouped_by_major.index, autopct='%1.1f%%', startangle=140)

plt.title('不同群科別的畢業生人數分佈')
plt.axis('equal')  # 使圓餅圖比例相等
plt.savefig('pic7.jpg')
