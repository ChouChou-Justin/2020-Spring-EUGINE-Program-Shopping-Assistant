import datetime
from pymongo import MongoClient

def ExportData(product_name, product_price):
    client = MongoClient('mongodb://localhost:27017')
    db = client['Prices']
    collection = db['{}'.format(product_name)]

    collection.insert_one({'Product': product_name,
                           'Price': product_price,
                           'Date': datetime.datetime.now()})

    cursor = collection.find().sort([('Date', -1)]).limit(1)
    data = [d for d in cursor]
    latestPrice = data[0]['Price']

    return float(latestPrice)

def allPrice(product_name):
    allPrice = []
    client = MongoClient('mongodb://localhost:27017')
    db = client['Prices']
    collection = db['{}'.format(product_name)]

    cursor = collection.find().sort([('Date', -1)])
    data = [d for d in cursor]

    for i in range(len(data)):
        allPrice.append([data[i]['Price'], data[i]['Date']])

    return allPrice

def Export_camelcamelcamel_top_price_drops_last_x_day(category, price_drop_of, x, minimum_type, _type, i, title, current_price, decreased_price, original_price, percentage, link, published, Id):
    client = MongoClient('mongodb://localhost:27017')
    db = client['Prices']
    collection = db['camelcamelcamel.com Top Amazon Price Drops']
    if _type != 2:
        collection.insert_one({'Category': category,
                               'Drop type': _type,
                               'Last x day(s)': x,
                               'Post {}'.format(i): title,
                               'Current price': current_price,
                               'Decreased price': decreased_price,
                               'Original price': original_price,
                               'Percentage': percentage,
                               'Link': link,
                               'Published': published,
                               'Id': Id})
    else:
        if minimum_type == 0:
            collection.insert_one({'Category': category,
                                   'Drop type': _type,
                                   'Minimum': minimum_type,
                                   'Price drop of $': price_drop_of,
                                   'Last x day(s)': x,
                                   'Post {}'.format(i): title,
                                   'Current price': current_price,
                                   'Decreased price': decreased_price,
                                   'Original price': original_price,
                                   'Percentage': percentage,
                                   'Link': link,
                                   'Published': published,
                                   'Id': Id})
        else:
            collection.insert_one({'Category': category,
                                   'Drop type': _type,
                                   'Minimum': minimum_type,
                                   'Price drop of %': price_drop_of,
                                   'Last x day(s)': x,
                                   'Post {}'.format(i): title,
                                   'Current price': current_price,
                                   'Decreased price': decreased_price,
                                   'Original price': original_price,
                                   'Percentage': percentage,
                                   'Link': link,
                                   'Published': published,
                                   'Id': Id})
    
def Export_camelcamelcamel_popular_product(category, i, title, link, current_price, list_price, avg_price, label, published):
    client = MongoClient('mongodb://localhost:27017')
    db = client['Prices']
    collection = db['camelcamelcamel.com Amazon popular products']
    collection.insert_one({'Category': category,
                           'Post {}'.format(i): title,
                           'Current price': current_price,
                           'List price': list_price,
                           'Average price': avg_price,
                           'Link': link,
                           'Label': label,
                           'Published': published})

def Export_slickdeals_certain_product(publishedTime, price, link, title, author):
    client = MongoClient('mongodb://localhost:27017')
    db = client['Prices']
    collection = db['SSD 256GB History Price']
    collection.insert_one({'Published Time': datetime.datetime.strptime(publishedTime, '%Y-%m-%d %H:%M:%S'),
                           'Price': price,
                           'Link': link,
                           'Title': title,
                           'Author': author})
    
def Export_all_prices(time, price, title, label):
    client = MongoClient('mongodb://localhost:27017')
    db = client['Prices']
    collection = db['All prices']
    if label == 0:
        collection.insert_one({'Date': datetime.datetime.now(),
                               'Price': price,
                               'Product': title,
                               'Source': 'Amazon'})
    elif label ==1:
        collection.insert_one({'Date': datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S'),
                               'Price': price,
                               'Product': title,
                               'Source': 'Slickdeals'})
    
def AtlasMongoDB(time, price, title, label):
    client = MongoClient('mongodb+srv://Senior_project:t106360211t106360229@cluster0-y0apq.mongodb.net/test?retryWrites=true&w=majority')
    db = client['Prices']
    collection = db['All prices']
    
    if label == 0:
        collection.insert_one({'Date': datetime.datetime.now(),
                               'Price': price,
                               'Product': title,
                               'Source': 'Amazon'})
    elif label ==1:
        collection.insert_one({'Date': datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S'),
                               'Price': price,
                               'Product': title,
                               'Source': 'Slickdeals'})

def Get_price_from_Atlas_mongoDB():
    client = MongoClient('mongodb+srv://Senior_project:t106360211t106360229@cluster0-y0apq.mongodb.net/test?retryWrites=true&w=majority')
    db = client['Prices']
    collection = db['All prices']
    
    cursor = collection.find()
    data = [d for d in cursor]
    
    return data