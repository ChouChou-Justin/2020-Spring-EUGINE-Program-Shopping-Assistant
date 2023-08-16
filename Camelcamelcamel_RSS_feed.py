import feedparser
import Database as DB
import RegularExpression as RE

def Get_top_price_drop():
    top_price_drop_categories = ['', 'appliances', 'apps-for-android', 'arts-crafts-sewing',
                                 'automotive', 'baby-products', 'beauty', 'books', 'cell-phones-accessories',
                                 'clothing-accessories', 'collectibles-fine-art', 'credit-cards', 
                                 'electronics', 'everything-else', 'gift-cards', 'grocery-gourmet-food',
                                 'health-personal-care', 'home-kitchen', 'industrial-scientific',
                                 'jewelry', 'kindle-store', 'magazine-subscriptions', 'movies-tv',
                                 'mp3-downloads', 'music', 'musical-instruments', 'office-products', 
                                 'other', 'patio-lawn-garden', 'pet-supplies', 'purchase-circles',
                                 'shoes', 'software', 'spine', 'sports-outdoors', 'tools-home-improvement',
                                 'toys-games', 'video-games', 'watches']
    
    drop_type = ['absolute', 'relative', 'recent']
    minimum_type = 'absolute'
    price_drop_of = 0.01
    
    print('Categories: \t0.All', '\t\t\t1.Appliances', '\t\t2.Apps for Android', '\t3.Arts crafts sewing\n',
          '\t\t4.Automotive', '\t\t5.Baby products', '\t6.Beauty', '\t\t7.Books\n', '\t\t8.Cell phones accessories',
          '9.Clothing accessories', '10.Collectibles fine art', '11.Credit cards\n', 
          '\t\t12.Electronics', '\t\t13.Everything else', '\t14.Gift cards', '\t\t15.Grocery gourmet food\n',
          '\t\t16.Health personal care', '17.Home kitchen', '\t18.Industrial scientific',
          '19.Jewelry\n', '\t\t20.Kindle store', '\t21.Magazine subscriptions', '22.Movies tv',
          '\t\t23.Mp3 downloads\n', '\t\t24.Music', '\t\t25.Musical instruments', '\t26.Ooffice products', 
          '\t27.Other\n', '\t\t28.Patio lawn garden', '\t29.Pet supplies', '\t30.Purchase circles',
          '\t31.Shoes\n', '\t\t32.Software', '\t\t33.Spine', '\t\t34.Sports outdoors', '\t35.Tools home improvement\n',
          '\t\t36.Toys games', '\t\t37.Video games', '\t\t38.Watches')
    bn = int(input('Choose category:'))
    
    print('\nDrop type: \t0.Biggest absolute price drops', '\t1.Biggest relative price drops', '\t2.Most recent price drops')
    t = int(input('Choose drop type:'))
    if t == 2:
        print('\nminimum type: \t0.Absolute \t1.Relative')
        s = int(input('Choose minimum type:'))
        minimum_type = s
        if s == 0:
            d = float(input('Price drop of $: '))
            price_drop_of = d
        else:
            d = float(input('Price drop of %: '))
            price_drop_of = d
           
    category = top_price_drop_categories[bn]
    _type = drop_type[t]

    for x in range(1,8):
        NewsFeed = feedparser.parse("https://camelcamelcamel.com/top_drops/feed?bn={}&d={}&i={}&s={}&t={}&".format(category, price_drop_of, x, minimum_type, _type))
        print('camelcamelcamel.com Top Amazon Price Drops Last {} Day------------------------------------'.format(x))
        number_of_rss_posts = NewsFeed.entries
        print('Number of RSS posts :', len(number_of_rss_posts))
        entry = NewsFeed.entries[0] 
        print('\n', entry.keys())
        
        for i in range(len(number_of_rss_posts)):
            entry = NewsFeed.entries[i]
            title = entry.title
            link = entry.link
            published = entry.published
            Id = entry.id
            price = RE.GetPrice(title)
            decreased_price = price[0]
            current_price = price[1]
            original_price = price[2]
            percentage = RE.GetPercentage(title)
            
            print('\nPost {}'.format(i))
            print('\nTitle {}:'.format(i), title)
            print('\nCurrent price {}:'.format(i), current_price) 
            print('\nDecreased price {}:'.format(i), decreased_price) 
            print('\nOriginal price {}:'.format(i), original_price) 
            print('\nDecreased percentage:'.format(i), percentage)
            print('\nLink {}:'.format(i), link)
            print('\nPublished {}:'.format(i), published)
            print('\nId {}:'.format(i), Id)
            print('--------------------------------------------------------------')
            if bn == 0:        
                category = 'All'
            DB.Export_camelcamelcamel_top_price_drops_last_x_day(category, price_drop_of, x, minimum_type, _type,
                                                                 i, title, 
                                                                 current_price, 
                                                                 decreased_price, 
                                                                 original_price,
                                                                 percentage, 
                                                                 link, 
                                                                 published, 
                                                                 Id) 

def Get_popular_products():
    popular_product_categories = ['', 'appliances', 'apps-for-android', 'arts-crafts-sewing',
                                 'automotive', 'baby-products', 'beauty', 'books', 'cell-phones-accessories', 
                                 'electronics', 'everything-else', 'gift-cards', 'grocery-gourmet-food',
                                 'health-personal-care', 'home-kitchen', 'industrial-scientific',
                                 'magazine-subscriptions', 'movies-tv', 'mp3-downloads', 'music',
                                 'musical-instruments', 'office-products', 'other',
                                 'patio-lawn-garden', 'pet-supplies', 'software', 'spine', 
                                 'sports-outdoors', 'tools-home-improvement',
                                 'toys-games', 'video-games']
    
    deal = ['All products', 'Deals only']
    
    print('Categories: \t0.All', '\t\t\t1.Appliances', '\t\t2.Apps for Android', '\t3.Arts crafts sewing\n',
          '\t\t4.Automotive', '\t\t5.Baby products', '\t6.Beauty', '\t\t7.Books\n', '\t\t8.Cell phones accessories', 
          '9.Electronics', '\t10.Everything else', '\t11.Gift cards\n', '\t\t12.Grocery gourmet food',
          '13.Health personal care', '14.Home kitchen', '\t15.Industrial scientific\n',
          '\t\t16.Magazine subscriptions', '17.Movies tv', '\t\t18.Mp3 downloads',
          '\t19.Music\n', '\t\t20.Musical instruments', '\t21.Ooffice products', 
          '\t22.Other', '\t\t23.Patio lawn garden\n', '\t\t24.Pet supplies',
          '\t25.Software', '\t\t26.Spine', '\t\t27.Sports outdoors\n', '\t\t28.Tools home improvement',
          '29.Toys games', '\t30.Video games')
    bn = int(input('Choose category:'))
    print('\nDeals: \t0.All product', '\t1.Deals only')
    deal = int(input('Choose Deals:'))
    
    if bn ==0:
        NewsFeed = feedparser.parse("https://camelcamelcamel.com/popular.xml?deal={}".format(deal))
        print('\ncamelcamelcamel.com popular products')
        number_of_rss_posts = NewsFeed.entries
        print('Number of RSS posts :', len(number_of_rss_posts))
        entry = NewsFeed.entries[0] 
        print('\n', entry.keys())
        category = 'All'
    else:
        NewsFeed = feedparser.parse("https://camelcamelcamel.com/popular.xml?deal={}&bn={}".format(deal, popular_product_categories[bn]))
        print('\ncamelcamelcamel.com popular products')
        number_of_rss_posts = NewsFeed.entries
        print('Number of RSS posts :', len(number_of_rss_posts))
        entry = NewsFeed.entries[0] 
        print('\n', entry.keys())
        category = popular_product_categories[bn]
        
    for i in range(len(number_of_rss_posts)):
        entry = NewsFeed.entries[i]
        title = entry.title
        link = entry.link
        published = entry.published
        summary = entry.summary
        price = RE.GetPrice(summary)
        current_price = price[0]
        list_price = price[1]
        avg_price = price[2]
        label = RE.GetLabel(summary, current_price, list_price, avg_price)
            
        print('\nPost {}'.format(i))
        print('\nTitle {}:'.format(i), title)
        print('\nLink {}:'.format(i), link)
        print('\nCurrent price {}:'.format(i), current_price) 
        print('\nList price {}:'.format(i), list_price) 
        print('\nAverage price {}:'.format(i), avg_price)
        if label != 0:
            print('\nLabel {}:'.format(i), label)
        print('\nPublished {}:'.format(i), published)
        print('--------------------------------------------------------------')

        DB.Export_camelcamelcamel_popular_product(category, i, title, link, 
                                                  current_price, list_price,
                                                  avg_price, label, published) 


def main():
    Get_popular_products()
    Get_top_price_drop()
main()