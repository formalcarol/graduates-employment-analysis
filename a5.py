import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

# 讀取資料
df = pd.read_csv('data7-1.csv')

# 按照公私立分組，計算每個分組的未升學就業人數總和
school_type_unemployed = df.groupby('設立別')['未升學就業人數'].sum()

# 繪製圓餅圖
plt.figure(figsize=(8, 8))

# 繪製圓餅圖，調整標籤位置和百分比位置
plt.pie(school_type_unemployed, labels=school_type_unemployed.index, autopct='%1.2f%%', startangle=90, labeldistance=1.1)

plt.title('公私立學校未升學就業人數比例')
plt.axis('equal')  # 使圓餅圖比例相等
plt.savefig('pic5.jpg')
