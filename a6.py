import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

# 讀取資料
df = pd.read_csv('data7-1.csv')

# 按照不同原因分組，計算每個原因的未升學就業人數總和
selected_reasons = ['正在接受職業訓練人數', '正在軍中服役人數', '需要工作而未找到人數', '補習或準備升學人數', '健康不良在家休養人數', '準備出國人數']
reason_unemployed = df[selected_reasons].sum()

# 繪製圓餅圖
plt.figure(figsize=(10, 8))

# 繪製圓餅圖，調整標籤位置和百分比位置
plt.pie(reason_unemployed, labels=reason_unemployed.index, autopct='%1.2f%%')

plt.title('未升學就業人數原因分佈')
plt.axis('equal')  # 使圓餅圖比例相等
plt.savefig('pic6.jpg')
