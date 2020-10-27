import pandas as pd
df = pd.read_csv (r'shopping.csv', encoding = 'utf-8', sep = ", \n", engine = 'python')
df.to_json (r'shopping.json')
