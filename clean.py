import os
import pandas as pd

# 處理"性別3"的資料
file_list = ['102_1_2_3.csv', '103_1_2_3.csv', '104_1_2_3.csv', '105_1_2_3.csv', '106_1_2_3.csv', '107_1_2_3.csv', '108_1_2_3.csv', '109_1_2_3.csv', '110_1_2_3.csv']
dfs = []
for file in file_list:
    df = pd.read_csv('dataset/' + file)
    year = int(file.split('_')[0])

    # 102-108需要補上學年度
    if year <= 108:
        df.insert(0, '學年度', year)

    # 原始資料的值名稱不同
    df['學程別'] = df['學程別'].replace({'專業群(職業)科':'專業群科', '進修部(學校)':'進修部'})
    df['設立別'] = df['設立別'].replace({'縣市立':'國立'})
    df = df[df['性別'] != '計']
    df.insert(5, '未升學就業人數', df.iloc[:, 5:11].sum(axis=1))
    dfs.append(df)

# 102-110所有資料連接在一起，成為data3.csv
combined_df = pd.concat(dfs, ignore_index=True)
combined_df = combined_df.iloc[:, :12]          # 刪掉第12個以後的屬性(比率)
grouped_df = combined_df.groupby(combined_df.columns[:4].tolist())[combined_df.columns[4:]].sum().reset_index() # 條件相同的資料合併
grouped_df.to_csv('data3-1.csv', index=False)

# 處理"地區7"的資料
file_list = ['102_1_2_7.csv', '103_1_2_7.csv', '104_1_2_7.csv', '105_1_2_7.csv', '106_1_2_7.csv', '107_1_2_7.csv', '108_1_2_7.csv', '109_1_2_7.csv', '110_1_2_7.csv']
dfs = []
for file in file_list:
    df = pd.read_csv('dataset/' + file)
    year = int(file.split('_')[0])

    # 102-108需要補上學年度
    if year <= 108:
        df.insert(0, '學年度', year)
    
    # 原始資料的屬性名稱不同
    if year <= 103:
        df.rename(columns={'學校所在地':'學校所在地別'}, inplace=True) 
    
    # 原始資料的屬性名稱不同
    df['學校所在地別'] = df['學校所在地別'].replace({'桃園縣':'桃園市', '新竹縣':'新竹市', '嘉義縣':'嘉義市', '連江縣':'外島', '澎湖縣':'外島', '金門縣':'外島'})
    df['設立別'] = df['設立別'].replace({'縣市立':'國立'})
    df.insert(4, '未升學就業人數', df.iloc[:, 4:10].sum(axis=1))
    dfs.append(df)

# 102-110所有資料連接在一起，成為data7.csv
combined_df = pd.concat(dfs, ignore_index=True)
combined_df = combined_df.iloc[:, :11]          # 刪掉第11個以後的屬性(比率)
grouped_df = combined_df.groupby(combined_df.columns[:3].tolist())[combined_df.columns[3:]].sum().reset_index() # 條件相同的資料合併
grouped_df.to_csv('data7-1.csv', index=False)

# 處理"群科11"的資料
file_list = ['102_1_2_11.csv', '103_1_2_11.csv', '104_1_2_11.csv', '105_1_2_11.csv', '106_1_2_11.csv', '107_1_2_11.csv', '108_1_2_11.csv', '109_1_2_11.csv', '110_1_2_11.csv']
dfs = []
for file in file_list:
    df = pd.read_csv('dataset/' + file)
    year = int(file.split('_')[0])

    # 102-108需要補上學年度
    if year <= 108:
        df.insert(0, '學年度', year)

    # 原始資料的屬性名稱不同
    if year <= 103:
        df.drop(columns=["學程分流"], inplace=True)
        df.rename(columns={'群別':'群科別'}, inplace=True) 
    
    # 原始資料的值名稱不同
    df['群科別'].fillna('學術群', inplace=True)
    df['群科別'] = df['群科別'].replace({'普通科':'學術群', '其他(綜合)':'綜合', '服務群':'家政群', '學術學程':'學術群'})
    df['學程別'] = df['學程別'].replace({'專業群(職業)科':'專業群科', '職業科':'專業群科', '進修部(學校)':'進修部'})
    df['設立別'] = df['設立別'].replace({'縣市立':'國立'})
    df.insert(5, '未升學就業人數', df.iloc[:, 5:11].sum(axis=1))
    dfs.append(df)

# 102-110所有資料連接在一起，成為data11.csv
combined_df = pd.concat(dfs, ignore_index=True)
combined_df = combined_df.iloc[:, :12]          # 刪掉第12個以後的屬性(比率)
grouped_df = combined_df.groupby(combined_df.columns[:4].tolist())[combined_df.columns[4:]].sum().reset_index() # 條件相同的資料合併
grouped_df.to_csv('data11-1.csv', index=False)
