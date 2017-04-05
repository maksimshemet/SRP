from spyre import server

import pandas as pd
import json

class UserUploadApp(server.App):

  title = "Custom File Upload Example"

  inputs = [{		"type":'dropdown',
					"label": 'Company', 
					"options" : [ {"label": "VHI", "value":"VHI"},
								  {"label": "TCI", "value":"TCI"},
								  {"label": "VCI", "value":"VCI"}],
					"value":'VHI',
					"key": 'ticker', 
					"action_id": "update_data"}]

  controls = [{ "type" : "upload",
          "id" : "ubutton"

        },
        { "type" : "button",
          "label" : "refresh",
          "id" : "update_data"},
          {	"type" : "hidden",
					"id" : "update_data"}
          
          ]

  tabs = [ "Text", "Table", "Plot"]

  outputs = [{  "type" : "plot",
          "id" : "plot",
          "control_id" : "update_data",
          "tab" : "Plot",
          "on_page_load" : False },
          
        { "type" : "table",
          "id" : "table_id",
          "control_id" : "update_data",
          "tab" : "Table",
          "on_page_load" : False },
        { "type" : "html",
          "id" : "html1",
          "control_id" : "update_data",
          "tab" : "Text"}]

  def __init__(self):
    self.upload_data = None
    self.upload_file = None

  def html1(self,params):
    text = "Upload a CSV and press refresh. There's a sample csv in the examples directory that you could try."
    if self.upload_data is not None:
      text = self.upload_data     
    return text

  def storeUpload(self,file):
    self.upload_file = file
    self.upload_data = file.read()

  def getData(self, params):
    
    df = None
    if self.upload_file is not None:
      self.upload_file.seek(0)
      df = pd.read_csv(self.upload_file)
      
    return df

  def getPlot(self, params):
  		
    df = self.getData(params)
    ticker = params['ticker']
    df1 = df[['year','week',ticker]]
    fig = df1.set_index('year').drop(['week'],axis=1).plot()
    fig.set_ylabel("week")

    fig.set_title(ticker)
    return fig

if __name__ == '__main__':
  app = UserUploadApp()
  app.launch(port=8090)