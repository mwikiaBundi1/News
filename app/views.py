#from .request import api_key, get_News, get_News_url, search_news
from .request import *
from flask import render_template, request, redirect, url_for

#from app import app

from .models import news
from.models import news

from app import app
from .models import review
from .forms import ReviewForm
Review = review.Review

# Views
@app.route('/')
def index():
    from .request import api_key, search_news
    sports = search_news('sports', api_key)
    technology = search_news('technology', api_key)
    health = search_news('health', api_key)
    general = search_news('general', api_key)
    entertainment = search_news('entertainment', api_key)


    '''
    View root page function that returns the index page and its data
    '''
    #assert(None not in (sports, technology, health, general, entertainment))

    title = 'MY NEWS PLATFORM'

    search_news = request.args.get('news_query')
    #print(search_news);exit(0)

    if search_news:
        return redirect(url_for('search',news_name=search_news))
    else:
        #return render_template('index.html', title=title, sports=sports)
        return render_template('index.html',title = title, sports=sports, technology = technology, health = health, general = general, entertainment = entertainment)

@app.route('/articles/<int:id>')
def articles(id):

     articles = get_News_url(id)
     title = f'{articles.title}'

     return render_template('articles.html',title = title,articles = articles)

@app.route('/search')
def search():

    sports = get_News('sports')
    technology = get_News('technology')
    health = get_News('health')
    general = get_News('general')
    entertainment = get_News('entertainment')

    '''
    View root page function that returns the index page and its data
    '''


    title = 'MY NEWS PLATFORM'
    return render_template('search.html',title = title, sports=sports, technology = technology, health = health, general = general, entertainment = entertainment)