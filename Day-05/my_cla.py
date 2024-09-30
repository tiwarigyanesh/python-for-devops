import sys

def sum(a, b):
    sum = a + b
    #print("the sum of number is " + str(sum))
    return sum

a = float(sys.argv[1])
operation = sys.argv[2]
b = float(sys.argv[3])

if operation == "sum" or operation == "add" or operation == "plus" or operation == "+" :
  output = sum(a , b)
  print (output)