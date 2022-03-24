import numpy as np
import csv
import plotly.express as px

def plotFigure(dataPath):
    with open(dataPath) as csvFile:
        dataFrames = csv.DictReader(csvFile)
        figure = px.scatter(dataFrames, x = "Size of TV", y = "Average time spent watching TV in a week (hours)")
        figure.show()

#function definition to restructure the data in terms of x and y
def getDataSource(dataPath):
    sizeOfTV = []          
    timeSpent = []
    with open(dataPath) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            sizeOfTV.append(float(row["Size of TV"]))
            timeSpent.append(float(row["Average time spent watching TV in a week (hours)"]))

    return{"x" : sizeOfTV, "y" : timeSpent}         

#function definition to find correlation value between two factors
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between the size of TV and hours spent watching TV :-  \n--->", correlation[0,1])

#function definition to calculate correlation between the given data
def setup():
    dataPath = "tv.csv"  

    #function call to restructure the data in terms of x and y  
    dataSource = getDataSource(dataPath)

    #function call to find correlation value between two factors
    findCorrelation(dataSource)

    plotFigure(dataPath)

#function call to calculate correlation between the given data
setup()    
