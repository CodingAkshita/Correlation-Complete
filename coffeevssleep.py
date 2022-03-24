import plotly.express as px #for graph
import csv
import numpy as np

def plotFigure(dataPath):
    with open(dataPath) as csvFile:
        dataFrames = csv.DictReader(csvFile)
        figure = px.scatter(dataFrames, x = "Coffee in ml", y = "sleep in hours")
        figure.show()

#function definition to restructure the data in terms of x and y
def getDataSource(dataPath):
    coffeeInML = []            
    sleepInHours = []
    with open(dataPath) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            coffeeInML.append(float(row["Coffee in ml"]))
            sleepInHours.append(float(row["sleep in hours"]))

    return{"x" : coffeeInML, "y" : sleepInHours}

#function definition to find correlation value between two factors
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])  
    print("Correlation between Coffee(ml) and sleep in hours = ", correlation[0,1])  

#function definition to calculate correlation between the given data
def setup():
    dataPath = "coffee.csv"  

    #function call to restructure the data in terms of x and y  
    dataSource = getDataSource(dataPath)

    #function definition to find correlation value between two factors
    findCorrelation(dataSource)

    plotFigure(dataPath)

#function definition to calculate correlation between the given data
setup()    