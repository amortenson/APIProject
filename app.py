from flask import Flask,request,url_for,redirect,render_template
import urllib2, json

app=Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def main():
    foods = []
    foods .append({'flavors': [0.16666666666666666, 0.16666666666666666, 0.5, 0.5, 0.8333333333333334, 0.8333333333333334], 'image': 'http://lh3.ggpht.com/-E7i4PyfgWJJC86wxhveIHfoHCgSOv3X_DZWqhUMpFPyJ9ekC52P14utMUdwycJeSGcbepqulf0c9G3aSArVFg=s90', 'name': "Mel's Red Hot Baked Wings"})
    foods.append({'flavors': [0.16666666666666666, 0.16666666666666666, 0.8333333333333334, 0.8333333333333334, 0.8333333333333334, 0.3333333333333333], 'image': 'http://lh5.ggpht.com/lSY2GG8Bcnl1Yxi-SAGMZZJU3xubiRNioCXiGmDYwZsK3PaYx7eRZZq1W5c7xVAgAsiMyY-Eqh9vTIEa11Yk4L0=s90', 'name': 'Jalepeno-Cheddar Bread'})
    foods.append({'flavors': [1.0, 0.3333333333333333, 0.5, 1.0, 0.0, 0.5], 'image': 'http://lh3.ggpht.com/KXYD08_3wKQ4lpnA_dlUJepU5MQssvMxjC8_M-lQ-vq0FtNAmasbfk7qV-yhh2PCzXAPZ0pdx4gXsg9Ph1zu7ks=s90', 'name': 'Double-Chocolate Brownies'})
    foods.append({'flavors': [0.8333333333333334, 0.16666666666666666, 0.5, 0.16666666666666666, 0.0, 0.6666666666666666], 'image': 'http://lh3.ggpht.com/VxetWazyJ4YUOjy8p9qhS7K5-VJABJ8jN1aXQAgSZgUMH5eBm3SMuCal1NM93NA3XBzAYzdIAK8Yu7zJhOij=s90', 'name': 'Red Velvet Cake'})
    foods.append({'flavors': [0.3333333333333333, 0.8333333333333334, 0.8333333333333334, 0.8333333333333334, 0.8333333333333334, 0.6666666666666666], 'image': 'http://lh3.ggpht.com/QS5Lual_Lm5XfwdrQx4PVJ6bk0pVWC1D672pe3rjRYS7otl2AlGta4cObB32J6Ok061cAepR9qVzU-Vy5WNy=s90', 'name': 'Chile Rellenos Bake'})
    foods.append({'flavors': [1.0, 1.0, 1.0, 0.6666666666666666, 0.0, 0.8333333333333334], 'image': 'http://lh3.ggpht.com/A1KtKWFGQ2CGAcE1dgpS5jfgvRZhl_c-G5l7KsiFWzit6VOPvKvxZG7odXi52ocDZyR7S6N7KBL2TZU_SSUCHg=s90', 'name': 'Strawberry Shortcake'})
    foods.append({'flavors': [0.6666666666666666, 0.6666666666666666, 0.8333333333333334, 0.6666666666666666, 0.0, 0.5], 'image': 'http://lh3.ggpht.com/Nt539GIfOiDBAPdMLtRwKOyKXmI_XazWx1vnJ7NilrKg5xYGvgLDiHCL3W7PefHR79CXGGtLImAfPDCSxV7tFrs=s90', 'name': 'My Favorite Buttermilk Biscuits'})
    foods.append({'flavors': [0.16666666666666666, 0.8333333333333334, 0.16666666666666666, 0.8333333333333334, 0.0, 0.3333333333333333], 'image': 'http://lh3.ggpht.com/n-TjpfGs5W2c_l79Zo1RlLd-E1G6Gt452FBMSzSM1LyzhpJx59FB-dm_8XJkF1fz4exN1Csbk9h0pr_6GJgK-lM=s90', 'name': 'Garlic Knots'}) 
    foods.append({'flavors': [0.6666666666666666, 1.0, 0.5, 0.3333333333333333, 0.0, 0.16666666666666666], 'image': 'http://lh6.ggpht.com/0CPJQy4X-doRS9VtZaMrI2HkLGMCaNwUqlqM5cxrPNBfwFWoFgqgPzUMUz0DEAvy821aRixZ5bjjrEB-Yip_0Lc=s90', 'name': 'Dead Simple Slaw'})
    foods.append({'flavors': [0.5, 0.3333333333333333, 0.5, 0.5, 0.0, 0.8333333333333334], 'image': 'http://lh3.ggpht.com/daLmPWVvNR466D8m_tKF9uGg7rw6eCFXKKzqprMkoUXHI9faUctEIppYYeHd3ZP0phM7inUj8ZAZLXzqnfbT=s90', 'name': '5 Minute Homemade Mac and Cheese'})
    attribution="Recipe search powered by <a href='http://www.yummly.com/recipes'><img alt='Yummly' src='http://static.yummly.com/api-logo.png'/></a>"
    if request.method == "GET":
        return render_template("base.html", foods=foods, attribution=attribution)
    else:
        return render_template("base.html", foods=foods, attribution=attribution)


if __name__=="__main__":
   app.debug=True
   app.run() 
