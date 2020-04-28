from app import app
from .models import news
import urllib.request
import json
News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']


# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]
source_url = app.config['SOURCE_API_BASE_URL']

def get_News(category):
    '''
    Function that gets the json response to our url request
    '''
    get_News_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_News_url) as url:
        get_News_data = url.read()
        get_News_response = json.loads(get_News_data)

        News_results = None

        if get_News_response['articles']:
            News_results_list = get_News_response['articles']
            News_results = process_results(News_results_list)


    return News_results

def process_results(news_list):        
    News_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')
        urlToImage = news_item.get('urlToImage')

        
        News_object = News(id,name,author,title,description,url,publishedAt,content,urlToImage)
        News_results.append(News_object)

    return News_results

def get_News_url(id):
    '''
    Function that gets the json response to our url request
    '''
    get_News_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_News_details_url) as url:
        get_News_details_data = url.read()
        get_News_details_response = json.loads(get_News_details_data)

        Object_results = None
        if get_News_details_response:
            id = get_News_details_response.get('id')
            name = get_News_details_response.get('name')
            author = get_News_details_response.get('author')
            title = get_News_details_response.get('title')
            description = get_News_details_response.get('description')
            url = get_News_details_response.get('url')
            publishedAt = get_News_details_response.get('publishedAt')
            content = get_News_details_response.get('content')
            urlToImage = get_News_details_response.get('urlToImage')
        
            Object_results=News(id,name,author,title, description, url, publishedAt, content, urlToImage)
        # # if get_News_details_response['articles']:
        #     News_results_list = get_News_details_response['articles']
        #     News_results = process_results(News_results_list)


    return Object_results

def search_news(news_name, _api_key):
    search_news_url = 'http://newsapi.org/v2/top-headlines?q={}&apiKey={}'.format(news_name, _api_key)
    #print(search_news_url);exit(0)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['articles'] and search_news_response['totalResults'] !=0:
            search_news_list = search_news_response['articles']
            search_news_results = process_results(search_news_list)
        else:
            print("No data retrieved!")
        


    return search_news_results


if __name__ == '__main__':
    pass