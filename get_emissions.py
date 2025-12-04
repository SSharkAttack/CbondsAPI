import requests
import pandas as pd
import json

url_emissions = 'https://ws.cbonds.info/services/json/get_emissions/?lang=eng'

json_data_emissions = {
        "auth": {"login": "Test", "password": "Test"},
        #"filters":[{"field":"currency_id","operator":"eq","value":"2"},{"field":"currency_id","operator":"eq","value":"2"} ],
        "fields":[{"field": "id"}, {"field": "isin_code"}],
        "sorting": [{"field": "id", "order": "asc"}]
    }


response = requests.get(url_emissions, data=json.dumps(json_data_emissions))
response_emissions = response.json()

#DataFrame
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

initial_dict = response_emissions.get('items', [])
df = pd.DataFrame(initial_dict)
print(df)

#To CSV file
#file_name = "cbonds_index_types.csv"
#df.to_csv(file_name, index=False)