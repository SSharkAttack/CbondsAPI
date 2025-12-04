import requests
import pandas as pd
import json

url_emissions = 'https://ws.cbonds.info/services/json/get_tradings_new/?lang=eng'

json_data_emissions = {
        "auth": {"login": "Test", "password": "Test"},
        #"filters":[{"field":"isin_code","operator":"eq","value":"XS0528414377"}],
        "fields":[{"field": "id"}, {"field": "emission_id"}, {"field": "indicative_price"}, {"field": "date"}, {"field": "isin_code"},{"field": "trading_ground_id"}],
        "sorting": [{"field": "date", "order": "desc"}]
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
#file_name = "cbonds_tradings.csv"
#df.to_csv(file_name, index=False)