from flask import Flask,request,url_for,redirect,render_template
import urllib2, json, random

app=Flask(__name__)

def randomfoods(i):
    result = ""
    foods = []
    for n in range(1):
        foods+=randomfoodshelper(i)
    for food in foods:
        result+=food['name']
        result+='<img src="'
        result+=str(food['image'])
        result+='"></img>'
        result+=str(food['distance'])        
        result+="<br>"
    result+=str(foods)
    return result
    #result+=str(tuple(values))
    #attribution=(results['attribution']['html'])

def randomfoodshelper(i):
    foods = []
    bounds = []
    values = []
    random.seed()
    random.random()
    random.random()
    for n in range(6):
        r = random.random()
        values.append(r)
        bounds.append(r-0.4)
        bounds.append(r+0.4)
    url = "http://api.yummly.com/v1/api/recipes?_app_id=9bb0bd30&_app_key=9e7a1eeeae374a6f14d388e755204848&flavor.sweet.min=%i&flavor.sweet.max=%i&flavor.piquant.min=%i&flavor.piquant.max=%i&flavor.salty.min=%i&flavor.salty.max=%i&flavor.meaty.min=%i&flavor.meaty.max=%i&flavor.sour.min=%i&flavor.sour.max=%i&flavor.bitter.min=%i&flavor.bitter.max=%i&requirePictures=true&maxresult=10" % tuple(bounds)
    request = urllib2.urlopen(url)
    res_string = request.read()
    results = json.loads(res_string)
    print results
    for match in results['matches']:
        thisfood = {}
        distance = 0
        if 'smallImageUrls' in match.keys():
            thisfood['image'] = (match['smallImageUrls'][0])
        if 'flavors' in match.keys():
            distance += ((match['flavors']['sweet']-values[0])**2)+((match['flavors']['piquant']-values[1])**2)+((match['flavors']['salty']-values[2])**2)
            distance += ((match['flavors']['meaty']-values[3])**2)+((match['flavors']['sour']-values[4])**2)+((match['flavors']['bitter']-values[5])**2)
            thisfood['distance'] = distance
            thisfood['flavors']=[0,0,0,0,0,0]
            thisfood['flavors'][0] = (match['flavors']['sweet'])
            thisfood['flavors'][1] = (match['flavors']['sour'])
            thisfood['flavors'][2] = (match['flavors']['salty'])
            thisfood['flavors'][3] = (match['flavors']['bitter'])
            thisfood['flavors'][4] = (match['flavors']['piquant'])
            thisfood['flavors'][5] = (match['flavors']['meaty'])
        if 'recipeName' in match.keys():
            thisfood['name'] = (match['recipeName'])
        
        foods.append(thisfood)
    return sorted(foods)[:i]
    #return foods

@app.route("/")
def index():
    return randomfoods(2)

if __name__=="__main__":
   app.debug=True
   app.run()

