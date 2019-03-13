#TASKS (4p)
#1 calculate & print the value of function y = 2x^2 + 2x + 2 for x=[56, 57, ... 100] (0.5p)

x= list(range(56,101))
y= []

for i in x:
    y.append(2*(i^2) + 2*i + 2)

print(y)

#2 ask the user for a number and print its factorial (1p)
#
#x= input("Write a number: ")
#x= int(x)
#for i in range(1,x):
#    x=x*i
#print("Fractional of this number is:", x)
#
#
#3 write a function which takes an array of numbers as an input and finds the lowest value. Return the index of that element and its value (1p)

x= [4,5,2,9,1,2]
def lowest_number(list):
    list.sort()
    print("Lowest number is: ", list[0])
lowest_number(x)

#4 looking at lab1-input and lab1-plot files create your own python script that takes a number and returns any chart of a given length.
#the length of a chart is the input to your script. The output is a plot (it doesn't matter if it's a y=x or y=e^x+2x or y=|x| function, use your imagination)

def plot(length):
    y = e ^ x + 2
    x = linspace(-10., 10., 200)

#test your solution properly. Look how it behaves given different input values. (1p)
#5 upload the solution as a Github repository. I suggest creating a directory for the whole python course and subdirectories lab1, lab2 etc. (0.5p)
#Ad 5 Hint write in Google "how to create a github repo". There are plenty of tutorials explaining this matter.