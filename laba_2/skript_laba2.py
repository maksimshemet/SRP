from spyre import server
import pandas as pd
from urllib.request import urlopen
import json
import datetime
import matplotlib.pyplot as plt


class StockExample(server.App):
    title = "Индексы чего-то непонятного"

    inputs = [{         
                    "type":'dropdown',
                    "label": 'Области', 
                    "options" : [ {"label": "Cherkasy", "value":"1"},
                                  {"label": "Chernihiv", "value":"2"},
                                  {"label": "Chernivtsi", "value":"3"},
                                  {"label": "Crimea", "value":"4"},
                                  {"label": "Dnipropetrovs'k", "value":"5"},
                                  {"label": "Donets'k", "value":"6"},
                                  {"label": "Ivano-Frankivs'k", "value":"7"},
                                  {"label": "Kharkiv", "value":"8"},
                                  {"label": "Kherson", "value":"9"},
                                  {"label": "Khmel'nyts'kyy", "value":"10"},
                                  {"label": "Kiev", "value":"11"},
                                  {"label": "Kiev City", "value":"12"},
                                  {"label": "Kirovohrad", "value":"13"},
                                  {"label": "Luhans'k", "value":"14"},
                                  {"label": "L'viv", "value":"15"},
                                  {"label": "Mykolayiv", "value":"16"},
                                  {"label": "Odessa", "value":"17"},
                                  {"label": "Poltava", "value":"18"},
                                  {"label": "Rivne", "value":"19"},
                                  {"label": "Sevastopol", "value":"20"},
                                  {"label": "Sumy", "value":"21"},
                                  {"label": "Ternopil", "value":"22"},
                                  {"label": "Transcarpathia", "value":"23"},
                                  {"label": "Vinnytsya", "value":"24"},
                                  {"label": "Volyn", "value":"25"},
                                  {"label": "Zaporizhzhya", "value":"26"},
                                  {"label": "Zhytomyr", "value":"27"}],
                    "key": 'ticker1', 
                    "action_id": "update_data"},
                    {
                    "type":'dropdown',
                    "label": 'Индексы', 
                    "options" : [ {"label": "VCI", "value":"VCI"},
                                  {"label": "TCI", "value":"TCI"},
                                  {"label": "VHI", "value":"VHI"}],
                    "key": 'ticker', 
                    "action_id": "update_data"

                    }]


    controls = [{   "type" : "hidden",
                    "id" : "update_data"}]

    tabs = ["Plot", "Table"]

    outputs = [{ "type" : "plot",
                    "id" : "plot",
                    "control_id" : "update_data",
                    "tab" : "Plot"},
                { "type" : "table",
                    "id" : "table_id",
                    "control_id" : "update_data",
                    "tab" : "Table",
                    "on_page_load" : True }]

    def getData(self, params):
        ticker = params['ticker1']
        # make call to yahoo finance api to get historical stock data
        url = "https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID={}&year1=1981&year2=2017&type=Mean".format(ticker)
       	result = urlopen(url).read()
       	data = json.loads(result.decode("utf8").replace('finance_charts_json_callback( ','')[:-1])
       	self.company_name = data['meta']['Company-Name']
		
       	return data

    def getPlot(self, params):
        ticker = params['ticker']
        df = pd.read_csv(name, index_col=False, header=1, skipfooter=1, engine='python',
                 names=['year', 'week', 'SMN', 'SMT', 'VCI', 'TCI', 'VHI'], delimiter='\,\s+|\s+|\,')
        
        plt.style.use('ggplot')
        return df[ticker].plot()

app = StockExample()
app.launch(port=9093)