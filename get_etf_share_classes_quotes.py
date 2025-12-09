   import requests
import pandas as pd
import json
import os
import openpyxl

url_emissions = 'https://ws.cbonds.info/services/json/get_etf_share_classes_quotes/?lang=eng'

json_data_emissions = {
        "auth": {"login": "Test", "password": "Test"},
        #"filter":[{"field":"isin","operator":"in","value":"LI1341568817;IE00B53SZB19;FR0010010827;AT0000497227;LI0399611693;"
                                                          #"AT0000A2R0P1;LI0445024057;FR001400K3S7;AT0000817952;AT0000A3FW41;"
                                                          #"LU2207278073;DE000A40A516;LU2327434507;FR0010510800;LI1403619219;"
                                                          #"LU0344810915;AT0000A1Z049;LI0477123637"}],
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

#To CSV file
df.to_excel(file_name, index=False)
print(f"Data saved to {file_name}")