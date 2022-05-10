import requests



STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "API KEY"

class StocksCrypto:
    def __init__(self):
        self.data ={}
        self.current_day = 0
        self.previous_day = 0
        self.diff  = 0
        
    
    def get_response(self,function,symbol, market = None):
        self.parasm = {
            "function" : function,
            'symbol': symbol,
            'market': market,
            "apikey" : STOCK_API_KEY,}
        response =  requests.get(STOCK_ENDPOINT, params=self.parasm)
        return response.json()


    def get_diff(self, strng, data):
        current_data = [value for (key, value) in data.items()]
        current_day = float(current_data[0][strng]) 
        previous_day = float(current_data[1][strng])
        diff = ((current_day - previous_day)/current_day)*100
        return round(current_day,2), round(previous_day,2), round(diff,2)

    def get_crypto(self, symbol):
        self.data = self.get_response("DIGITAL_CURRENCY_DAILY", symbol, market = 'EUR')["Time Series (Digital Currency Daily)"]
        self.current_day, self.previous_day, self.diff = self.get_diff('4a. close (EUR)', self.data)
        return symbol, self.current_day, self.previous_day, self.diff
        

    def get_stocks(self, stock):
        self.parasm = {
            "function" : 'TIME_SERIES_DAILY',
            'symbol': stock,
            'outputsize': 'compact',
            'datatype': 'json',
            "apikey" : STOCK_API_KEY,}
        response =  requests.get(STOCK_ENDPOINT, params=self.parasm)
        self.data = response.json()['Time Series (Daily)']
        self.current_day, self.previous_day, self.diff = self.get_diff('4. close', self.data)
        return stock, self.current_day, self.previous_day, self.diff



