import math
from guizero import App, Drawing
from copy import deepcopy
import random
import timeit

tes = [
    [-4500, -4400],
    [-4100, -3000],
    [-1800, -2400],
    [-2500, -3400],
    [-2000, -1400],

    [+4500, -4400],
    [+4100, -3000],
    [+1800, -2400],
    [+2500, -3400],
    [+2000, -1400],
    
    [-4500, +4400],
    [-4100, +3000],
    [-1800, +2400],
    [-2500, +3400],
    [-2000, +1400],

    [+4500, +4400],
    [+4100, +3000],
    [+1800, +2400],
    [+2500, +3400],
    [+2000, +1400]
]
test = []

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.col = ""
        self.dist = 10000


def initTest():
    for i in range(20):
        test.append(point(tes[i][0], tes[i][1]))
        if i < 5:
            test[i].col = "red"
        elif i < 10:
            test[i].col = "green"
        elif i < 15:
            test[i].col = "blue"
        else:
            test[i].col = "purple"

def getDist(a, b):
    sideA = abs(a.x - b.x)
    sideB = abs(a.y - b.y)
    dist = sideA**2 + sideB**2
    return dist
def classify(x, y, k):
    temp = point(x, y)
    distances = test
    counter = [0,0,0,0]

    for i in distances:
        i.dist = getDist(temp, i)
    
    distances.sort(key=lambda x: x.dist)

    for i in distances[:k]:
        if i.col == "red":
            counter[0] += 1
        elif i.col == "green":
            counter[1] += 1
        elif i.col == "blue":
            counter[2] += 1
        else:
            counter[3] += 1
    
    top = max(counter)

    if counter[0] == top:
        temp.col = "red"
    elif counter[1] == top:
        temp.col = "green"
    elif counter[2] == top:
        temp.col = "blue"
    else:
        temp.col = "purple"
    
    return temp
    

def generate(col):
    bad = (99 == random.randrange(0,100))

    if col == 0:    #generate red
        if bad:
            return(random.randrange(-5000, 5001), random.randrange(-5000, 5001))
        else:
            return(random.randrange(-5000, 501), random.randrange(-5000, 501))
    elif col == 1:  #generate green
        if bad:
            return(random.randrange(-5000, 5001), random.randrange(-5000, 5001))
        else:
            return(random.randrange(-500, 5001), random.randrange(-5000, 501))
    elif col == 2:  #generate blue
        if bad:
            return(random.randrange(-5000, 5001), random.randrange(-5000, 5001))
        else:
            return(random.randrange(-5000, 501), random.randrange(-500, 5001))
    elif col == 3:  #generate purple
        if bad:
            return(random.randrange(-5000, 5001), random.randrange(-5000, 5001))
        else:
            return(random.randrange(-500, 5001), random.randrange(-500, 5001))
def show():
    app = App()
    app.height = 1000
    app.width = 1000
    drawing = Drawing(app, width=1000, height=1000)
    for i in test:
        x = (i.x + 5000)/10
        y = (i.y + 5000)/10
        drawing.oval(x, y, x + 7, y + 7, i.col)
    app.display()


def main():
    numOfPoints = int(input("How many points are we generating?\n"))
    result = [0, 0]
    points = []
    klist = [1, 3, 7, 15]
    for i in range(numOfPoints):
        points.append(generate(i % 4))

    for j in klist:
        test.clear()
        initTest()
        result = [0, 0]
        start = timeit.default_timer()
        for i in range(len(points)):
            #A loading printout
            if i % 100 == 0:
                print(i)

            temp = classify(points[i][0], points[i][1], j)

            if i%4 == 0:
                if temp.col == "red":
                    result[0] += 1
                else:
                    result[1] += 1
            elif i%4 == 1:
                if temp.col == "green":
                    result[0] += 1
                else:
                    result[1] += 1
            elif i%4 == 2:
                if temp.col == "blue":
                    result[0] += 1
                else:
                    result[1] += 1
            elif i%4 == 3:
                if temp.col == "purple":
                    result[0] += 1
                else:
                    result[1] += 1

            test.append(temp)
        print("K{}:{} {} ==> {}%".format(j, result[0], result[1], result[0]/(numOfPoints/100)))
        stop = timeit.default_timer()
        print("It took {:.4f} seconds to run.".format(stop - start))
        show()
    
    

start = timeit.default_timer()
main()
stop = timeit.default_timer()
print("It took {:.4f} seconds to run.".format(stop - start))

