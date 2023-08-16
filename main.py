import time
import Scraper
import Mail
import Database
import PlotFigure

email = Mail.EnterRecipient()

def main(emailAddress):
     URLs = ['https://www.amazon.com/Samsung-250GB-Internal-MZ-76E250B-AM/dp/B07864WMK8/ref=sr_1_1?dchild=1&keywords=samsung+SSD+256gb&qid=1586843379&sr=8-1']
    
     for URL in URLs:
         product_name, product_price = Scraper.GetPrice(URL=URL)
         latest_price = Database.ExportData(product_name=product_name, product_price=product_price)
         Database.Export_all_prices(time=0, price=product_price, title=product_name, label=0)
         Database.AtlasMongoDB(time=0, price=product_price, title=product_name, label=0)
         if product_price != latest_price:
             Mail.SendMail(productName=product_name, productPrice=product_price, latestPrice=latest_price, mail=emailAddress)
         print('Product: ', product_name)
         print('Price: ', product_price)
         allPrice = Database.allPrice(product_name)
         if len(allPrice) % 10 == 0:
             PlotFigure.PlotPriceFigure(allPrice=allPrice, product_name=product_name)

while(True):
    main(emailAddress=email)
    time.sleep(60)
