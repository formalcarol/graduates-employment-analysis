import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

# 讀取資料
df = pd.read_csv('data3-1.csv')

# 按年度和原因分組，計算人數總和
yearly_reason_totals = df.groupby(['學年度']).sum()

# 選擇您感興趣的原因列
selected_reasons = ['正在接受職業訓練人數', '正在軍中服役人數', '需要工作而未找到人數', '補習或準備升學人數', '健康不良在家休養人數', '準備出國人數']

# 繪製折線圖
plt.figure(figsize=(10, 6))
for reason in selected_reasons:
    plt.plot(yearly_reason_totals.index, yearly_reason_totals[reason], marker='o', label=reason)

plt.title('原因vs年度')
plt.xlabel('學年度')
plt.ylabel('人數')
plt.xticks(yearly_reason_totals.index)  # 設置 x 軸刻度為學年度
plt.legend()
plt.grid(True)
plt.savefig('pic3.jpg')
