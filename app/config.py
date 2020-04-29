class Config:

    '''
    General configuration parent class
        '''
    # NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&apiKey={}'
    # ARTICLE_API_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
    # NEWS_API_KEY = os.environ.get('NEWS_API_KEY') 

    NEWS_API_BASE_URL= 'http://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'
    SOURCE_API_BASE_URL ='https://newsapi.org/v2/sources?apiKey={}'
    pass



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True