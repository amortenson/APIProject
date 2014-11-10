from flask import Flask,request,url_for,redirect,render_template
import urllib2, json, random

app=Flask(__name__)

def randomfoods(i):
    foods = []
    values = []
    result = ""
    random.seed()
    random.random()
    random.random()
    for n in range(6):
        r = random.random()
        values.append(r-0.3)
        values.append(r+0.3)
    url = "http://api.yummly.com/v1/api/recipes?_app_id=9bb0bd30&_app_key=9e7a1eeeae374a6f14d388e755204848&flavor.sweet.min=%i&flavor.sweet.max=%i&flavor.piquant.min=%i&flavor.piquant.max=%i&flavor.salty.min=%i&flavor.salty.max=%i&flavor.meaty.min=%i&flavor.meaty.max=%i&flavor.sour.min=%i&flavor.sour.max=%i&flavor.bitter.min=%i&flavor.bitter.max=%i&requirePictures=true" % tuple(values)
    request = urllib2.urlopen(url)
    res_string = request.read()
    results = json.loads(res_string)
    for match in results['matches']:
        if 'smallImageUrls' in match.keys():
            foods+=(match['smallImageUrls'])
    for food in foods:
        result+='<img src="'
        result+=food
        result+='"></img>'
    result+=str(tuple(values))
    attribution=(results['attribution']['html'])
    return result

@app.route("/")
def index():
    return randomfoods(5)

if __name__=="__main__":
   app.debug=True
   app.run()

