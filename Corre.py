import numpy as np
import csv

def dataSource(data_path) :
    coffee = []
    hours = []
    with open(data_path) as f :
        csv_reader = csv.DictReader(f)
        for row in csv_reader :
            coffee.append(float(row['Coffee in ml']))
            hours.append(float(row['sleep in hours']))
    return {'x':coffee , 'y':hours}

def correlation(data_source) :
    correlation_find = np.corrcoef(data_source['x'],data_source['y'])
    print('The correlation between the coffee in ml and the sleep hours is  :' , correlation_find[0,1])

def setup() :
    data_path = 'C:/Users/Dixit/Chitrarath Dixit Dropbox/CHITRARATH DIXIT/PC\Desktop/Python/Pro-106/coffee-sleep.csv'
    data_source = dataSource(data_path)
    correlation(data_source)

setup()