import pandas as pd
import time

df = pd.read_csv('data.txt', sep='\t')
df2 = pd.read_excel('Sku2Asin.xlsx')

df['date'] = 0
df['month'] = 0
df['asin'] = 0
dcount = 0
acount = 0
bcount = 0

for n in df['purchase-date']:
    temp = n.split("T")
    date_temp = temp[0].split("-")[2]
    df.date[dcount] = date_temp
    df.month[dcount] = temp[0].split("-")[1]
    dcount += 1

for n in df['sku']:
    for m in df2['SKU']:
        if n == m:
            df.asin[acount] = df2.Asin[bcount]
            #print(df.asin[acount], df2.Asin[bcount])

        bcount += 1
    acount += 1
    bcount = 0

for m in df2['Asin']:
    # print(df2.Asin[bcount])
    bcount += 1


df_final = df[['purchase-date', 'buyer-name',
               'buyer-phone-number', 'sku', 'shipment-status', 'date', 'month', 'asin']]
#df_final = df_final.loc[df['shipment-status'] == "Delivered to Buyer"]
df_final = df_final.loc[df['buyer-phone-number'] == " "]
print(df_final)
#df_final.to_excel(r'data.xlsx', index=False)
print("Convert Done")
time.sleep(5)
