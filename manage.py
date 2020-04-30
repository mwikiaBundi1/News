# from flask import Flask
# app=Flask(__name__)
# @app.route('/')
# def hello():
#     return "hello"
# if __name__ == '__main__':
#     app.run(debug = True)

# from urllib import request

from app import app
#print(dir(app.wsgi_app));exit()

if __name__== '__main__':
    app.run()



