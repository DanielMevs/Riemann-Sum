#1st arg=left endpoint, 2nd arg=right endpoint, n=number of subinteverals, f = function
import math
def right_riemann(x,y,n,f):
    dx = int((y-x)/n)
    s = 0 #sum
    for i in range(x,y): #functions as a sigma
        s = s + dx*(f(i+1))
    return s

def left_riemann(x,y,n,f):
    dx = int((y-x)/n)
    s= 0
    for i in range(x,y):
        s = s + dx*(f(i))
    return s

def midpoint_riemann(x,y,n,f):
    dx = ((y-x)/n)
    offset = dx/2
    s = 0
    for i in range(x,y):
        s = s + (dx*(f(i+offset)))
    return s

#eval(input("Please input a funtion in python-friendly notation"))

f = lambda x:-6-(math.pow(x,3))
n = 4

print("Midpoint riemann sum: ", midpoint_riemann(3,7,n,f))


print("Right riemann sum: ",right_riemann(3,7,n,f)) 
print("Left riemann sum: ",left_riemann(3,7,n,f))

'''
s1 = left_riemann(3,7,n,f)
s2 = right_riemann(3,7,n,f)
approximate_intergral =  ((s1 + s2)/2)'''
