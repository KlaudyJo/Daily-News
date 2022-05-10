import requests
#NEWS_ENDPOINT = "https://newsapi.org/v2/top-headlines"
NEWS_api_key = "API_KEY"


class Get_Current_News:
    def __init__(self):
        self.new_parasm = {}
        self.NEWS_ENDPOINT = "https://newsapi.org/v2/top-headlines"
        
    def get_news(self):
        self.new_parasm = {"apiKey": NEWS_api_key,'country' : 'cz','pageSize': 10,}
        response = requests.get(self.NEWS_ENDPOINT, params = self.new_parasm)

        articles = response.json()['articles']
        formated_articles = [f"Titul: {article['title']}.\n Opis :{article['description']}.\n URL: {article['url']}]" for article in articles]
        return formated_articles
