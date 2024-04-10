import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

# 讀取資料
df = pd.read_csv('data3-1.csv')

# yearly_totals 學年度 畢業生人數 未升學就業人數 未升學人數占比
yearly_totals = df.groupby('學年度')[['畢業生人數', '未升學就業人數']].sum().reset_index()
yearly_totals['未升學人數占比'] = yearly_totals['未升學就業人數'] / yearly_totals['畢業生人數'] * 100


# 繪製長條圖
plt.figure(figsize=(10, 6))
bars1 = plt.bar(yearly_totals['學年度'], yearly_totals['畢業生人數']-yearly_totals['未升學就業人數'], color='skyblue', label='已升學/就業人數')
bars2 = plt.bar(yearly_totals['學年度'], yearly_totals['未升學就業人數'], color='salmon', label='未升學/就業人數', bottom=yearly_totals['畢業生人數']-yearly_totals['未升學就業人數'])

# 在每個長條的上方顯示未升學人數占比
for bar1, bar2, percentage in zip(bars1, bars2, yearly_totals['未升學人數占比']):
    height = bar1.get_height() + bar2.get_height()
    plt.text(bar1.get_x() + bar1.get_width() / 2, height, f'{percentage:.2f}%', ha='center', va='bottom')

# 加入圖例、標題等
plt.xlabel('學年度')
plt.ylabel('人數')
plt.title('畢業生人數及未升學就業人數占比')
plt.legend()
plt.tight_layout()
plt.savefig('pic1.jpg')