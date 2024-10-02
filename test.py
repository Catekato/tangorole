import json
import pandas as pd

# 读取CSV文件，使用分号作为分隔符
df = pd.read_csv('/Users/yuyingxia/Desktop/val.csv', sep=';', header=None)

# 将列名重命名以匹配JSON键
df.columns = ["dataset", "location", "captions"]

# 将DataFrame转换为JSON格式
json_data = df.to_json(orient="records", default_handler=dict)

# 保存json文件
with open(r'/Users/yuyingxia/Desktop/valData.json', 'w') as jsonFile:
    jsonFile.write(json_data,)
# print(type(json_data))