import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn import linear_model

def LinearRegressionModel(time, price): 
    x = time
    y = price
    
    le = preprocessing.LabelEncoder()
    le.fit(x)
    labeled_x = le.transform(x)
    
    new_x = np.array(labeled_x).reshape(-1, 1)
    new_y = np.array(y).reshape(-1, 1)
    
    regression = linear_model.LinearRegression()
    regression.fit(new_x, new_y)

    plt.figure(figsize=(12, 12))
    plt.title('SSD 256GB Slickdeals historical price after dropping 70% of outliers with linear regression')
    plt.scatter(new_x, new_y, c='r', label='Prices')
    plt.plot(new_x, regression.predict(new_x), c='g', label='Linear Equation', linewidth=3)
    plt.xlabel('Time (Labeled)')
    plt.ylabel('Price (USD)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.savefig('SSD 256GB Slickdeals historical price after dropping 70 percent of outliers with linear regression.png')
    plt.show()

def LinearRegressionModel2(Slickdeals_time, Slickdeals_price, Amazon_time, Amazon_price, eBay_time, eBay_price): 
    x = Slickdeals_time
    y = Slickdeals_price
    
    le = preprocessing.LabelEncoder()
    le.fit(x)
    labeled_x = le.transform(x)
    
    new_x = np.array(labeled_x).reshape(-1, 1)
    new_y = np.array(y).reshape(-1, 1)
    
    regression = linear_model.LinearRegression()
    regression.fit(new_x, new_y)

    plt.figure(figsize=(12, 12))
    plt.title('SSD 256GB Slickdeals historical price after dropping 90% of outliers with linear regression')
    plt.scatter(new_x, new_y, c='r', label='Prices')
    plt.plot(new_x, regression.predict(new_x), c='g', label='Linear Equation', linewidth=3)
    plt.xlabel('Time (Labeled)')
    plt.ylabel('Price (USD)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.savefig('SSD 256GB Slickdeals historical price after dropping 90 percent of outliers with linear regression.png')
    plt.show()
        
    plt.figure(figsize=(12, 12))
    plt.title('SSD 256GB history price with linear regression and other sources')
    plt.scatter(eBay_time, eBay_price, c='blue', label='eBay Prices')
    plt.scatter(Amazon_time, Amazon_price, c='red', label='Amazon Prices')
    plt.plot(x, regression.predict(new_x), c='green', label='Linear Equation', linewidth=3)
    plt.xlabel('Time (Unlabeled)')
    plt.ylabel('Price (USD)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.savefig('SSD 256GB history price with linear regression and other sources.png')
    plt.show()
    
    
    
    
    
    
    
    