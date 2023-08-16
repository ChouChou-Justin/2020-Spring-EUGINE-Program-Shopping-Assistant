import datetime
import seaborn as sns
import LinearRegession as LR
import StandardDeviation as SD
import matplotlib.pyplot as plt
import RegularExpression as RE

def PlotPriceFigure(allPrice, product_name):
    figureName = RE.figureName(product_name=product_name)
    price = []
    time = []
    fig = plt.figure(figsize=(10, 10))
    plt.title('{}'.format(product_name))
    for i in range(len(allPrice)):
        price.append(allPrice[i][0])
        time.append(allPrice[i][1])
    plt.plot(time, price, 'r--')
    plt.title('The price of {}'.format(product_name))
    plt.xlabel('Time')
    plt.ylabel('Price (USD)')
    fig.savefig('{}-{}.png'.format(figureName, len(allPrice)))
    plt.show()
    plt.close(fig)

def PlotPriceHistory(dataset):
    avg = 0
    length = 0
    x = []
    y = []
    j = []
    k = []
    time = []
    price = []
    
    for i in range(len(dataset)):
        time.append(dataset[i][0])
        price.append(dataset[i][1])
    
    ax = sns.boxplot(price)
    
    temp_sort_by_time = [[time[i], price[i]] for i in range(len(time))]
    temp_sort_by_price = [[price[i], time[i]] for i in range(len(time))]
    temp_sort_by_time.sort()
    temp_sort_by_price.sort()
    
    j_temp = []
    
    for i in range(len(temp_sort_by_time)):
        j_temp.append(temp_sort_by_time[i][0])
        k.append(temp_sort_by_time[i][1])
        
    for item in j_temp:
        j.append(datetime.datetime.strptime(item[0:10], '%Y-%m-%d'))
        
    plt.figure(figsize=(12, 12))
    plt.title('SSD 256GB Slickdeals historical price before dropping outliers')
    plt.scatter(j, k, c='r', label='Prices')
    plt.xlabel('Time')
    plt.ylabel('Price (USD)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.savefig('SSD 256GB Slickdeals historical price before dropping outliers.png')
    plt.show()
    
    mean_before_dropping_outliers, standard_deviation_before_dropping_outliers = SD.Calculate_standard_deviation(prices=price)
    print('Mean before dropping outliers: ', mean_before_dropping_outliers)
    print('Standard Deviation before dropping outliers:', standard_deviation_before_dropping_outliers)
    
    temp_sort_by_price = temp_sort_by_price[0:int(round(len(temp_sort_by_price)*0.3, 0))]
    temp_sort_by_price = sorted(temp_sort_by_price, key=lambda item: item[1])
    
    for i in range(len(temp_sort_by_price)-1):
        date = temp_sort_by_price[i][1][0:10]
        next_date = temp_sort_by_price[i+1][1][0:10]
        if (i == len(temp_sort_by_price)-2)&(date == next_date):
            avg = temp_sort_by_price[i][0]+temp_sort_by_price[i+1][0]
            length = length + 2
            avg = round(avg/length, 2)
            x.append(datetime.datetime.strptime(date, '%Y-%m-%d'))
            y.append(avg)
        elif (i == len(temp_sort_by_price)-2)&(date != next_date):
            avg = avg+temp_sort_by_price[i][0]
            length = length + 2
            avg = round(avg/length, 2)
            x.append(datetime.datetime.strptime(date, '%Y-%m-%d'))
            y.append(avg)
            x.append(datetime.datetime.strptime(next_date, '%Y-%m-%d'))
            y.append(temp_sort_by_price[i+1][0])
        elif date == next_date:
            avg = avg+temp_sort_by_price[i][0]
            length = length + 1
        elif date != next_date:
            avg = avg+temp_sort_by_price[i][0]
            length = length + 1
            avg = round(avg/length, 2)
            x.append(datetime.datetime.strptime(date, '%Y-%m-%d'))
            y.append(avg)
            avg = 0
            length = 0

    plt.figure(figsize=(12, 12))
    plt.title('SSD 256GB Slickdeals historical price after dropping 70% of outliers')
    plt.scatter(x, y, c='r', label='Prices')
    plt.xlabel('Time')
    plt.ylabel('Price (USD)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.savefig('SSD 256GB Slickdeals historical price after dropping 70 percent of outliers.png')
    plt.show()
    
    ax = sns.boxplot(y)
    
    price = []
    time = []
     
    for _time_, _price_ in zip(x, y):
        price.append(_price_)
        time.append(_time_)
    
    mean_after_dropping_outliers_70, standard_deviation_after_dropping_outliers_70 = SD.Calculate_standard_deviation(prices=price)
    print('Mean after dropping 70% of data points as outliers: ', mean_after_dropping_outliers_70)
    print('Standard Deviation after dropping 70% of data points as outliers:', standard_deviation_after_dropping_outliers_70)
    
    LR.LinearRegressionModel(time, price)
    
def PlotEachPrice(dataset):
    Slickdeals_data = []
    eBay_data = []
    Amazon_data = []
    
    for item in dataset:
        if item['Source'] == 'Amazon':
            Amazon_data.append([item['Date'], item['Price']])
        elif item['Source'] == 'Slickdeals':
            Slickdeals_data.append([item['Date'], item['Price']])
        else:
            eBay_data.append([item['Date'], item['Price']])
#Slickdeals--------------------------------------------------------------------   
    avg = 0
    length = 0
    x = []
    y = []
    Slickdeals_time = []
    Slickdeals_price = []
    
    for i in range(len(Slickdeals_data)):
        Slickdeals_time.append(str(Slickdeals_data[i][0]))
        Slickdeals_price.append(Slickdeals_data[i][1])
        
    Slickdeals_price_sort_by_price = [[Slickdeals_price[i], Slickdeals_time[i]] for i in range(len(Slickdeals_time))]
    Slickdeals_price_sort_by_price.sort()
     
    Slickdeals_price_sort_by_price = Slickdeals_price_sort_by_price[0:int(round(len(Slickdeals_price_sort_by_price)*0.1, 0))]
    Slickdeals_price_sort_by_price = sorted(Slickdeals_price_sort_by_price, key=lambda item: item[1])
    
    for i in range(len(Slickdeals_price_sort_by_price)-1):
        date = Slickdeals_price_sort_by_price[i][1][0:10]
        next_date = Slickdeals_price_sort_by_price[i+1][1][0:10]
        if (i == len(Slickdeals_price_sort_by_price)-2)&(date == next_date):
            avg = Slickdeals_price_sort_by_price[i][0] + Slickdeals_price_sort_by_price[i+1][0]
            length = length + 2
            avg = round(avg/length, 2)
            x.append(datetime.datetime.strptime(date, '%Y-%m-%d'))
            y.append(avg)
        elif (i == len(Slickdeals_price_sort_by_price)-2)&(date != next_date):
            avg = avg + Slickdeals_price_sort_by_price[i][0]
            length = length + 2
            avg = round(avg/length, 2)
            x.append(datetime.datetime.strptime(date, '%Y-%m-%d'))
            y.append(avg)
            x.append(datetime.datetime.strptime(next_date, '%Y-%m-%d'))
            y.append(Slickdeals_price_sort_by_price[i+1][0])
        elif date == next_date:
            avg = avg + Slickdeals_price_sort_by_price[i][0]
            length = length + 1
        elif date != next_date:
            avg = avg + Slickdeals_price_sort_by_price[i][0]
            length = length + 1
            avg = round(avg/length, 2)
            x.append(datetime.datetime.strptime(date, '%Y-%m-%d'))
            y.append(avg)
            avg = 0
            length = 0
            
    plt.figure(figsize=(12, 12))
    plt.title('SSD 256GB Slickdeals historical price after dropping 90% of outliers')
    plt.scatter(x, y, c='r', label='Prices')
    plt.xlabel('Time')
    plt.ylabel('Price (USD)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.savefig('SSD 256GB Slickdeals historical price after dropping 90 percent of outliers.png')
    plt.show()
    
    Slickdeals_price = []
    Slickdeals_time = []
     
    for _time_, _price_ in zip(x, y):
        Slickdeals_price.append(_price_)
        Slickdeals_time.append(_time_)
        

#eBay--------------------------------------------------------------------------
    avg = 0
    length = 0
    x = []
    y = []
    eBay_time = []
    eBay_price = []
    
    for i in range(len(eBay_data)):
        eBay_time.append(str(eBay_data[i][0]))
        eBay_price.append(eBay_data[i][1])
        
    eBay_price_sort_by_price = [[eBay_price[i], eBay_time[i]] for i in range(len(eBay_time))]
    eBay_price_sort_by_price.sort()
     
    eBay_price_sort_by_price = eBay_price_sort_by_price[0:int(round(len(eBay_price_sort_by_price)*0.9, 0))]
    eBay_price_sort_by_price = sorted(eBay_price_sort_by_price, key=lambda item: item[1])
    
    for i in range(len(eBay_price_sort_by_price)-1):
        date = eBay_price_sort_by_price[i][1][0:10]
        next_date = eBay_price_sort_by_price[i+1][1][0:10]
        if (i == len(eBay_price_sort_by_price)-2)&(date == next_date):
            avg = eBay_price_sort_by_price[i][0] + eBay_price_sort_by_price[i+1][0]
            length = length + 2
            avg = round(avg/length, 2)
            x.append(datetime.datetime.strptime(date, '%Y-%m-%d'))
            y.append(avg)
        elif (i == len(eBay_price_sort_by_price)-2)&(date != next_date):
            avg = avg + eBay_price_sort_by_price[i][0]
            length = length + 2
            avg = round(avg/length, 2)
            x.append(datetime.datetime.strptime(date, '%Y-%m-%d'))
            y.append(avg)
            x.append(datetime.datetime.strptime(next_date, '%Y-%m-%d'))
            y.append(eBay_price_sort_by_price[i+1][0])
        elif date == next_date:
            avg = avg + eBay_price_sort_by_price[i][0]
            length = length + 1
        elif date != next_date:
            avg = avg + eBay_price_sort_by_price[i][0]
            length = length + 1
            avg = round(avg/length, 2)
            x.append(datetime.datetime.strptime(date, '%Y-%m-%d'))
            y.append(avg)
            avg = 0
            length = 0
    
    eBay_price = []
    eBay_time = []
     
    for _time_, _price_ in zip(x, y):
        eBay_price.append(_price_)
        eBay_time.append(_time_)
        
#Amazon------------------------------------------------------------------------    
    avg = 0
    length = 0
    x = []
    y = []
    Amazon_time = []
    Amazon_price = []
    
    for i in range(len(Amazon_data)):
        Amazon_time.append(str(Amazon_data[i][0]))
        Amazon_price.append(Amazon_data[i][1])
        
    Amazon_price_sort_by_price = [[Amazon_price[i], Amazon_time[i]] for i in range(len(Amazon_time))]
    Amazon_price_sort_by_price = sorted(Amazon_price_sort_by_price, key=lambda item: item[1])
    
    for i in range(len(Amazon_price_sort_by_price)-1):
        date = Amazon_price_sort_by_price[i][1][0:10]
        next_date = Amazon_price_sort_by_price[i+1][1][0:10]
        if (i == len(Amazon_price_sort_by_price)-2)&(date == next_date):
            avg = Amazon_price_sort_by_price[i][0] + Amazon_price_sort_by_price[i+1][0]
            length = length + 2
            avg = round(avg/length, 2)
            x.append(datetime.datetime.strptime(date, '%Y-%m-%d'))
            y.append(avg)
        elif (i == len(Amazon_price_sort_by_price)-2)&(date != next_date):
            avg = avg + Amazon_price_sort_by_price[i][0]
            length = length + 2
            avg = round(avg/length, 2)
            x.append(datetime.datetime.strptime(date, '%Y-%m-%d'))
            y.append(avg)
            x.append(datetime.datetime.strptime(next_date, '%Y-%m-%d'))
            y.append(Amazon_price_sort_by_price[i+1][0])
        elif date == next_date:
            avg = avg + Amazon_price_sort_by_price[i][0]
            length = length + 1
        elif date != next_date:
            avg = avg + Amazon_price_sort_by_price[i][0]
            length = length + 1
            avg = round(avg/length, 2)
            x.append(datetime.datetime.strptime(date, '%Y-%m-%d'))
            y.append(avg)
            avg = 0
            length = 0
    
    Amazon_price = []
    Amazon_time = []
     
    for _time_, _price_ in zip(x, y):
        Amazon_price.append(_price_)
        Amazon_time.append(_time_)
        
    mean_after_dropping_outliers_90, standard_deviation_after_dropping_outliers_90 = SD.Calculate_standard_deviation(prices=Slickdeals_price)
    print('Mean after dropping 90% of data points as outliers: ', mean_after_dropping_outliers_90)
    print('Standard Deviation after dropping 90% of data points as outliers:', standard_deviation_after_dropping_outliers_90)
    
    LR.LinearRegressionModel2(Slickdeals_time, Slickdeals_price, Amazon_time, Amazon_price, eBay_time, eBay_price)
        