import csv
import plotly.express as px 
import numpy as np

def plotFigure(dataPath):
    with open(dataPath) as csvFile:
        dataFrames = csv.DictReader(csvFile)
        figure = px.scatter(dataFrames, x = "Days Present", y = "Marks In Percentage")
        figure.show()

def getDataSource(dataPath):
    daysPresent = []
    MarksInPercentage = []
    with open(dataPath) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            daysPresent.append(float(row["Days Present"]))
            MarksInPercentage.append(float(row["Marks In Percentage"]))

    return{"x" : daysPresent, "y": MarksInPercentage}    

def findCorrelation(dataSource):        
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between the Days Present and marks in percentage :- \n--->", correlation[0,1])

def setup():
    dataPath = "student.csv"    
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)
    plotFigure(dataPath)

setup()    