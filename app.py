from flask import Flask,render_template
from bs4 import BeautifulSoup as SOUP 
import re 
import requests as HTTP

app = Flask(__name__)

app.debug = True
@app.route('/')
def index():
    return render_template('cover.html')
@app.route('/form')
def form():
    return render_template('index.html')
 
@app.route('/enjoy')
def enjoy():
    urlhere = 'https://www.imdb.com/search/title/?genres=thriller&title_type=tv_series,mini_series'
    arr=movie(urlhere,"Enjoy")
    return render_template("enjoy.html",url=urlhere,arr=arr)

@app.route('/anger')
def anger():
    urlhere = 'https://www.imdb.com/search/title/?genres=family&title_type=tv_series&sort=moviemeter,asc'
    arr=movie(urlhere,"Anger")  
    return render_template("enjoy.html",url=urlhere,arr=arr)

@app.route('/anticipation')
def anticipation():
     urlhere = 'https://www.imdb.com/search/title/?genres=thriller&title_type=tv_series,mini_series'
     arr=movie(urlhere,"Anticipation")
     return render_template("enjoy.html",url=urlhere,arr=arr)

@app.route('/surprise')
def surprise():
    urlhere = 'https://www.imdb.com/list/ls026503059/'
    arr=movie(urlhere,"Surprise")
    return render_template("enjoy.html",url=urlhere,arr=arr)

@app.route('/disgust')
def disgust():
    urlhere = 'https://www.imdb.com/search/title/?genres=musical&explore=title_type,genres&title_type=tvSeries'
    arr=movie(urlhere,"Disgust")
    return render_template("enjoy.html",url=urlhere,arr=arr)

@app.route('/sad')
def sad():
    urlhere = 'https://www.imdb.com/search/title/?genres=action&title_type=tv_series&sort=moviemeter'
    arr=movie(urlhere,"Sad")
    return render_template("enjoy.html",url=urlhere,arr=arr)

@app.route('/fear')
def fear():
    urlhere = 'https://www.imdb.com/search/title/?genres=sport&explore=title_type,genres&title_type=tvSeries'
    arr=movie(urlhere,"Fear")
    return render_template("enjoy.html",url=urlhere,arr=arr)

@app.route('/trust')
def trust():
    urlhere = 'https://www.imdb.com/search/title/?genres=western&explore=title_type,genres&title_type=tvSeries'
    arr=movie(urlhere,"Trust")
    return render_template("enjoy.html",url=urlhere,arr=arr)


def movie(urlhere,emotion):
    response = HTTP.get(urlhere) 
    data = response.text


    soup = SOUP(data, "lxml") 
          

    title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')}) 
    count = 0	
    k=0
    arr=[]
    if(emotion == "Disgust" or emotion == "Anger" or emotion=="Surprise"):
        for i in title:
            tmp = str(i).split('>')
            
            if(len(tmp) == 3):
                arr.append(tmp[1][:-3])

            if(count > 13):
                break
            count += 1
            
    else:
        for i in title:
            tmp = str(i).split('>') 
                
            if(len(tmp) == 3): 
                arr.append(tmp[1][:-3])
                  
            if(count > 11):
                break
            count+=1  
    return arr
app.run(host='localhost', port=5000)