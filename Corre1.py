import numpy as np
import csv 

def dataSource(data_path) :
    marks = []
    days = []
    with open(data_path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader : 
            marks.append(float(row['Marks In Percentage']))
            days.append(float(row['Days Present']))
    return{ 'x':marks , 'y':days }

def correlation(data_source) :
    correlation_find = np.corrcoef(data_source['x'],data_source['y'])
    print('The correlation between marks and days prent is  :' , correlation_find[0,1])

def setup() :
    data_path = 'C:/Users/Dixit/Chitrarath Dixit Dropbox/CHITRARATH DIXIT/PC/Desktop/Python/Pro-106/marks-days.csv'
    data_source = dataSource(data_path)
    correlation(data_source)

setup() 