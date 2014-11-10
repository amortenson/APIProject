from flask import Flask,request,url_for,redirect,render_template
import urllib2, json

app=Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def main():
    foods = []
    url = "http://api.yummly.com/v1/api/recipes?_app_id=9bb0bd30&_app_key=9e7a1eeeae374a6f14d388e755204848&flavor.sweet.min=0.8&flavor.sweet.max=1&flavor.piquant.min=0&flavor.piquant.max=0.2&requirePictures=true"
    request = urllib2.urlopen(url)
    res_string = request.read()
    results = json.loads(res_string)
    print results
    for match in results['matches']:
        if 'smallImageUrls' in match.keys():
            foods+=(match['smallImageUrls'])
    attribution=(results['attribution']['html'])
    return render_template("base.html", foods=foods, attribution=attribution)


if __name__=="__main__":
   app.debug=True
   app.run() 
