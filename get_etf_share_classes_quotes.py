import requests
import pandas as pd #for data frame
import json
import os #for Downloads path
import openpyxl #for xlsx file

url_emissions = 'https://ws.cbonds.info/services/json/get_etf_share_classes_quotes/?lang=eng'

json_data_emissions = {
        "auth": {"login": "Test", "password": "Test"},
        #"filter":[{"field":"isin","operator":"in","value":"LI1341568817;IE00B53SZB19;FR0010010827;AT0000497227;LI0399611693}],
        #"fields":[{"field": "id"}, {"field": "cupon_sum"}, {"field": "cupon_rate"}, {"field": "coupon_num"}, {"field": "emission_isin_code"}],
        "sorting": [{"field": "date", "order": "desc"}]
    }




response_emissions = requests.get(url_emissions, json=json_data_emissions).json()
print(response_emissions)

#DataFrame
initial_dict = response_emissions['items']
df = pd.DataFrame.from_dict(initial_dict)
print(df)

# Download Path
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
file_name = os.path.join(downloads_path, "cbonds_etf_quotes.xlsx")

#To XLSX file
df.to_excel(file_name, index=False)

print(f"Data saved to {file_name}")
