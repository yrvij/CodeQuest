from fractions import Fraction

function = input('Please enter a polynomial function (f(x)): ')
interval = input('Please enter an interval: ').strip('[]')
n = int(input('Please enter the number of rectangles to calculate the Riemann Sum Integral: '))

a,b = int(interval[:interval.index(',')]),int(interval[interval.index(',')+1:])
w = Fraction((b-a)/n)
x = w
sum = 0
while x <= b:
    sum += eval(function)
    x += w

print()
print('The area under the curve of f(x) = ' + str(float(round(sum*w,7))) + ' units' + u'\u00B2')
