import feedparser
import PlotFigure
import numpy as np
import Database as DB
import RegularExpression as RE

def Slickdeals_front_page():
    NewsFeed = feedparser.parse("https://slickdeals.net/newsearch.php?mode=frontpage&searcharea=deals&searchin=first&rss=1")
    print('Front page-----------------------------------------------------')
    number_of_rss_posts = NewsFeed.entries
    print('Number of RSS posts :', len(number_of_rss_posts))
    entry = NewsFeed.entries[0] 
    print('\n', entry.keys())
    
    for i in range(len(number_of_rss_posts)):
        entry = NewsFeed.entries[i]
        title = entry.title
        link = entry.link
        published = entry.published
        author = entry.author
        
        print('\nPost {}:'.format(i))
        print('\nTitle {}:'.format(i), title)
        print('\nLink {}:'.format(i), link)
        price = RE.GetPrice(title)
        for j in range(len(price)):
            print('\nPrice {}:'.format(i), price[j])
        print('\nPublished {}:'.format(i), published)
        print('\nAuthor {}:'.format(i), author)
        print('--------------------------------------------------------------')
        
def Slickdeals_popular_deals():
    NewsFeed = feedparser.parse("https://slickdeals.net/newsearch.php?mode=popdeals&searcharea=deals&searchin=first&rss=1")
    print('Popular deals-----------------------------------------------------')
    number_of_rss_posts = NewsFeed.entries
    print('Number of RSS posts :', len(number_of_rss_posts))
    entry = NewsFeed.entries[0] 
    print('\n', entry.keys())
    
    for i in range(len(number_of_rss_posts)):
        entry = NewsFeed.entries[i]
        title = entry.title
        link = entry.link
        published = entry.published
        author = entry.author
        
        print('\nPost {}:'.format(i))
        print('\nTitle {}:'.format(i), title)
        print('\nLink {}:'.format(i), link)
        price = RE.GetPrice(title)
        for j in range(len(price)):
            print('\nPrice {}:'.format(i), price[j])
        print('\nPublished {}:'.format(i), published)
        print('\nAuthor {}:'.format(i), author)
        print('--------------------------------------------------------------')

def Certain_product():
    product_name = RE.CheckProduct(product=input("Type in product: "))
    page = 1
    dataset = []
    deletePosition = []
    while(page <= 100):       
        NewsFeed = feedparser.parse('https://slickdeals.net/newsearch.php?rss=1&page={}&src=SearchBarV2&q={}&searcharea=deals&searchin=first'.format(page, product_name))
        number_of_rss_posts = NewsFeed.entries
        entry = NewsFeed.entries[0] 

        for i in range(len(number_of_rss_posts)):
            entry = NewsFeed.entries[i]
            title = entry.title
            link = entry.link
            published = entry.published
            author = entry.author
              
            print('\nTitle {}:'.format(i), title)
            print('\nLink {}:'.format(i), link)
            price = RE.GetPrice(title)
            for j in range(len(price)):
                print('\nPrice {}:'.format(i), price[j])
            print('\nPublished {}:'.format(i), published)
            print('\nAuthor {}:'.format(i), author)
            print('--------------------------------------------------------------')
            if len(price) != 0:
                dataset.append([published, price, link, title, author])     
        print('Page: ', page)
        page += 1

    for i in range(len(dataset)):
        dataset[i][0] = RE.ConvertDateForSlickdeals(dataset[i][0])
        dataset[i][1] = RE.ConvertPriceForSlickdeals(dataset[i][1])
        
    for pos, pr in enumerate(price):
        if pr == None:
            deletePosition.append(pos)
            
    for i in deletePosition:
        dataset.pop(i)
        for pos, j in enumerate(deletePosition):
            deletePosition[pos] = j-1
            
    for i in range(len(dataset)):
        dataset[i][1] = float(dataset[i][1])
        
#    for i in range(len(dataset)):
#        Database.Export_slickdeals_certain_product(dataset[i][0], dataset[i][1], dataset[i][2], dataset[i][3], dataset[i][4])
        
#    for i in range(len(dataset)):
#        Database.Export_all_prices(time=dataset[i][0], price=dataset[i][1], title=dataset[i][3], label=1)
        
#    for i in range(len(dataset)):
#        Database.AtlasMongoDB(time=dataset[i][0], price=dataset[i][1], title=dataset[i][3], label=1)
        
    PlotFigure.PlotPriceHistory(dataset)
    
def main():
#    Slickdeals_front_page()
#    Slickdeals_popular_deals()
    Certain_product()
    data = DB.Get_price_from_Atlas_mongoDB()
    data = np.array(data)
    PlotFigure.PlotEachPrice(data)
    

main()