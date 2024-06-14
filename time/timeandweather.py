from flask import Flask
from flask_cors import CORS
app= Flask(__name__)
CORS(app)
@app.route("/tandw")
def tandw():
    import requests
    import re
    import json
    from bs4 import BeautifulSoup
    from requests import Session
    import sys
    session=requests.Session()
    country=sys.argv[1]#input('Enter country: ').lower()
    city=sys.argv[2]#input('Enter city: ').lower()
    url="https://www.timeanddate.com/worldclock/"+country+"/"+city
    res1=session.get(url)
    res1,url
    soup=BeautifulSoup(res1.text,"html.parser")
    #print(soup)
    p=soup.find('span',attrs={'id':"ct"})
    tz=soup.find('span',attrs={'id':'cta'})
    date=soup.find('span',attrs={'id':'ctdat'})
    w=soup.find('div',attrs={'id':'wt-tp'})
    # print("Time in "+country+"'s "+"city is "+p.text+" "+tz.text)
    # print("Date:",date.text)
    # print("Weather in "+country+"'s "+city+" is "+w.text)
    l1=['time','date','temperature','climate']
    # print(p.text+tz.text)
    # print(date.text)
    # print(w.text)
    dv=soup.find_all('p',attrs={'class':None,'span':None,'id':None})
    for x in dv:
    #     condition=re.search('\s.\d',x.text)
        if(x.text[-1]=='C'):
            y=x.text
    l2=[]
    l2.append(p.text+" "+tz.text)
    l2.append(date.text)
    l2.append(w.text)
    l2.append(y)
    d=dict(zip(l1,l2))
    return d
if __name__=='__main__':
    app.run(debug=True)