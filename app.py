from flask import Flask,request,url_for,redirect,render_template
import urllib2, json

app=Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def main():
    foods = []
    foods.append({'id': 0, 'flavors': [0.16666666666666666, 0.16666666666666666, 0.5, 0.5, 0.8333333333333334, 0.8333333333333334], 'image': 'http://lh3.ggpht.com/-E7i4PyfgWJJC86wxhveIHfoHCgSOv3X_DZWqhUMpFPyJ9ekC52P14utMUdwycJeSGcbepqulf0c9G3aSArVFg=s90', 'name': "Mel's Red Hot Baked Wings"})
    foods.append({'id': 1,'flavors': [0.16666666666666666, 0.16666666666666666, 0.8333333333333334, 0.8333333333333334, 0.8333333333333334, 0.3333333333333333], 'image': 'http://lh5.ggpht.com/lSY2GG8Bcnl1Yxi-SAGMZZJU3xubiRNioCXiGmDYwZsK3PaYx7eRZZq1W5c7xVAgAsiMyY-Eqh9vTIEa11Yk4L0=s90', 'name': 'Jalepeno-Cheddar Bread'})
    foods.append({'id': 2,'flavors': [1.0, 0.3333333333333333, 0.5, 1.0, 0.0, 0.5], 'image': 'http://lh3.ggpht.com/KXYD08_3wKQ4lpnA_dlUJepU5MQssvMxjC8_M-lQ-vq0FtNAmasbfk7qV-yhh2PCzXAPZ0pdx4gXsg9Ph1zu7ks=s90', 'name': 'Double-Chocolate Brownies'})
    foods.append({'id': 3,'flavors': [0.8333333333333334, 0.16666666666666666, 0.5, 0.16666666666666666, 0.0, 0.6666666666666666], 'image': 'http://lh3.ggpht.com/VxetWazyJ4YUOjy8p9qhS7K5-VJABJ8jN1aXQAgSZgUMH5eBm3SMuCal1NM93NA3XBzAYzdIAK8Yu7zJhOij=s90', 'name': 'Red Velvet Cake'})
    foods.append({'id': 4,'flavors': [0.3333333333333333, 0.8333333333333334, 0.8333333333333334, 0.8333333333333334, 0.8333333333333334, 0.6666666666666666], 'image': 'http://lh3.ggpht.com/QS5Lual_Lm5XfwdrQx4PVJ6bk0pVWC1D672pe3rjRYS7otl2AlGta4cObB32J6Ok061cAepR9qVzU-Vy5WNy=s90', 'name': 'Chile Rellenos Bake'})
    foods.append({'id': 5,'flavors': [1.0, 1.0, 1.0, 0.6666666666666666, 0.0, 0.8333333333333334], 'image': 'http://lh3.ggpht.com/A1KtKWFGQ2CGAcE1dgpS5jfgvRZhl_c-G5l7KsiFWzit6VOPvKvxZG7odXi52ocDZyR7S6N7KBL2TZU_SSUCHg=s90', 'name': 'Strawberry Shortcake'})
    foods.append({'id': 6,'flavors': [0.6666666666666666, 0.6666666666666666, 0.8333333333333334, 0.6666666666666666, 0.0, 0.5], 'image': 'http://lh3.ggpht.com/Nt539GIfOiDBAPdMLtRwKOyKXmI_XazWx1vnJ7NilrKg5xYGvgLDiHCL3W7PefHR79CXGGtLImAfPDCSxV7tFrs=s90', 'name': 'My Favorite Buttermilk Biscuits'})
    foods.append({'id': 7,'flavors': [0.16666666666666666, 0.8333333333333334, 0.16666666666666666, 0.8333333333333334, 0.0, 0.3333333333333333], 'image': 'http://lh3.ggpht.com/n-TjpfGs5W2c_l79Zo1RlLd-E1G6Gt452FBMSzSM1LyzhpJx59FB-dm_8XJkF1fz4exN1Csbk9h0pr_6GJgK-lM=s90', 'name': 'Garlic Knots'}) 
    foods.append({'id': 8,'flavors': [0.6666666666666666, 1.0, 0.5, 0.3333333333333333, 0.0, 0.16666666666666666], 'image': 'http://lh6.ggpht.com/0CPJQy4X-doRS9VtZaMrI2HkLGMCaNwUqlqM5cxrPNBfwFWoFgqgPzUMUz0DEAvy821aRixZ5bjjrEB-Yip_0Lc=s90', 'name': 'Dead Simple Slaw'})
    foods.append({'id': 9,'flavors': [0.5, 0.3333333333333333, 0.5, 0.5, 0.0, 0.8333333333333334], 'image': 'http://lh3.ggpht.com/daLmPWVvNR466D8m_tKF9uGg7rw6eCFXKKzqprMkoUXHI9faUctEIppYYeHd3ZP0phM7inUj8ZAZLXzqnfbT=s90', 'name': '5 Minute Homemade Mac and Cheese'})
    attribution="Recipe search powered by <a href='http://www.yummly.com/recipes'><img alt='Yummly' src='http://static.yummly.com/api-logo.png'/></a>"
    if request.method == "GET":
        return render_template("base.html", foods=foods, test="moo",attribution=attribution, entered = False)
    else:
        empty=[]
        elements = 0
        flavors = [0,0,0,0,0,0]
        for item in request.form.items():
            for food in foods: #not optimized, but should be fine with short lists
                if food['id'] == int(item[0]):
                    elements+=int(item[1])
                    for i in range(6):
                        flavors[i]+=food['flavors'][i]*int(item[1])
         
        for i in range(6):
            if elements != 0:
                flavors[i] = flavors[i]/elements      
        test="sweet,sour,salty,bitter,piquant,meaty<br>"+str(flavors)  
        ran = []
        smallestdist = 5
        bestfood = {}
        print flavors
        for flavor in flavors:
            print flavor
            ran.append(flavor-0.2)
            ran.append(flavor+0.2)
        print tuple(ran)
        url = "http://api.yummly.com/v1/api/recipes?_app_id=9bb0bd30&_app_key=9e7a1eeeae374a6f14d388e755204848&flavor.sweet.min=%f&flavor.sweet.max=%f&flavor.sour.min=%f&flavor.sour.max=%f&flavor.salty.min=%f&flavor.salty.max=%f&flavor.bitter.min=%f&flavor.bitter.max=%f&flavor.piquant.min=%f&flavor.piquant.max=%f&flavor.meaty.min=%f&flavor.meaty.max=%f&requirePictures=true" % tuple(ran)
        req = urllib2.urlopen(url)
        res_string = req.read()
        results = json.loads(res_string)
        for match in results['matches']:
            thisfood = {}
            distance = 0
            if 'smallImageUrls' in match.keys():
                thisfood['image'] = (match['smallImageUrls'][0].strip('=s90'))
            if 'flavors' in match.keys():
                distance += ((match['flavors']['sweet']-flavors[0])**2)+((match['flavors']['sour']-flavors[1])**2)+((match['flavors']['salty']-flavors[2])**2)
                distance += ((match['flavors']['bitter']-flavors[3])**2)+((match['flavors']['piquant']-flavors[4])**2)+((match['flavors']['meaty']-flavors[5])**2)
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
            if distance < smallestdist:
                bestfood = thisfood
        print bestfood
        return render_template("base.html", foods=empty, test=bestfood,attribution=attribution, entered = True)


if __name__=="__main__":
   app.debug=True
   app.run() 
