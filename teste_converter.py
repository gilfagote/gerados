import pandas as pd
import json
import csv

with open ('shopping2.json') as json_file:
    data = json.load(json_file)
    
pedidos = data['order']

data_file = open ('shopping2.csv', 'w')

csv_writer = csv.writer(data_file, delimiter = '|')

count = 0

for ped in pedidos:
    if count == 0:

        header = ped.keys()
        csv_writer.writerow(header)
        count += 1

    csv_writer.writerow(ped.values())

data_file.close()

pedidoDf = pd.read_csv('shopping2.csv', sep = '|', engine = 'python')

pedidoDf['Total'] = pedidoDf['quantity'] * pedidoDf['value']

pedidodf = pedidoDf.append({'name': 'Total','Total': pedidoDf['Total'].sum()}, ignore_index = 'True') 

json_to_csv = pedidodf.to_csv('j_to_c.csv', sep = '|', index = 'True')

