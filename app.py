import os
from flask import Flask, Response, send_from_directory

def create_app():

    app = Flask('app', static_url_path='')

    @app.route('/style.css')
    def stylecss():
        return send_from_directory('.', 'style.css')

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory('.', 'favicon.ico', mimetype='image/vnd.microsoft.icon')    

    @app.route('/')
    def hello_world():
        response = Response()
        response.headers['link'] = '<style.css>; rel=stylesheet;'
        response.headers['Refresh'] = '5; url=https://www.youtube.com/watch?v=iUsecpG2bWI'
        return response

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=80, debug=True)    
