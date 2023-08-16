import re

def ConvertPrice(price):
    tempPrice = price[1:]
    if ',' in tempPrice:
        converted_price = tempPrice.replace(',', '')
    else:
        converted_price = tempPrice
            
    return float(converted_price)

        

def DetectMail(mail):
    correctMail = re.findall(r'([\w\-]+@[\w\.]+)', mail)

    return correctMail

def figureName(product_name):
    list = ['/', ':', '*', '?', '"', '<', '>', '|', '\\']
    for character in product_name:
        if character in list:
            product_name = product_name.replace(character, ' ')

    return product_name

def GetPrice(title):
    price = re.findall(r'(\$[\w\,\.]+)', title)
    for i in range(len(price)):
        if ',' in price[i]:
            price[i] = price[i].replace(',', '')
        else:
            price[i] = price[i]
    
    return price
  
def GetPercentage(title):
    percentage = re.findall(r'([\w\,\.]+\%)', title)
        
    return percentage[0]   

def GetLabel(summary, current_price, list_price, avg_price):
    label_best = re.findall(r'(Best Price)', summary)
    label_good = re.findall(r'(Good Deal)', summary)
    
    if label_best != []:
        return label_best[0]
    elif label_good != []:
        return label_good[0]
    elif (current_price > avg_price)&(current_price >= list_price):
        return 'Bad Deal'
    elif (current_price > avg_price)&(current_price < list_price):
        return 'Think about it'
    
def CheckProduct(product):
    product_name = product.replace(' ', '%20')
    
    return product_name

def TransformTime(time):
    time = re.findall(r'([\,\w]+\%)', time)
    
    return time[0]

def ConvertPriceForSlickdeals(prices):
    for price in prices:
        tempPrice = price[1:]
        if ',' in tempPrice:
            converted_price = tempPrice.replace(',', '')
            REPrice = re.findall(r'([\d]+[\.]*[\d]*)', converted_price)
        else:
            converted_price = tempPrice
            REPrice = re.findall(r'([\d]+[\.]*[\d]*)', converted_price)
            
        if len(REPrice) == 0:
            return None
        else:
            return REPrice[0]

def ConvertDateForSlickdeals(date):
    tempDate = date[5:-4]
    
    day = tempDate[0:2]
    month = tempDate[3:6]
    year = tempDate[7:11]
    hour = tempDate[12:14]
    minute = tempDate[15:17]
    second = tempDate[18:21]
    
    if month == 'Jan':
        month = '01'
    elif month == 'Feb':
        month = '02'
    elif month == 'Mar':
        month = '03'
    elif month == 'Apr':
        month = '04'
    elif month == 'May':
        month = '05'
    elif month == 'Jun':
        month = '06'    
    elif month == 'Jul':
        month = '07'    
    elif month == 'Aug':
        month = '08'   
    elif month == 'Sep':
        month = '09'    
    elif month == 'Oct':
        month = '10'    
    elif month == 'Nov':
        month = '11'    
    elif month == 'Dec':
        month = '12'
        
    return year + '-' + month + '-' + day + ' ' + hour + ':' + minute + ':' + second
    