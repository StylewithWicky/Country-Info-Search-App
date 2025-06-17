from flask import Flask,render_template,request
import requests
from config import Config

app=Flask(__name__)
app.config.from_object(Config)

@app.route('/' , methods=['GET'])

def index():
    new_data=None
    news=request.args.get('news')

    if news:
        api_key=app.config['NEW_API_KEY']
        url=f'hhttps://newsapi.org/v2/everything?q={news}&sortBy=publishedAt&apiKey={api_key}'
        response=requests.get(url)

    if response.status_code==200:
        data=response.json()
        articles= data.get('articles', [])

        if articles: 
            first=articles[0]  

            new_data={
            'author':first.get('author'),
            'name':first.get('name'),
            'title':first.get('title'),
            'description':first.get('description')

            }
        else:
            new_data={ 'error':'Could not find articles'}
    else:
        new_data={'error':'Failed to get news'}
    return render_template('index.html',news=new_data)

      
