import math
import time

def check_scalar_multiple(list1, list2):
    div_ = 0
    for i in range(len(list1)):
        if list2[i] != 0:
            div_ = list1[i]/list2[i] 
        else:
            continue
    
    for v in zip(list1[1:], list2[1:]):
        if v[0] != div_ * v[1]:
            return False
        else:
            continue
    return True

def parallelogram_checker(A,B,C,D):
    global isparallelogram 
    if check_scalar_multiple(A,B) and check_scalar_multiple(C,D):
        return True
    else:
        return False

def parallelogram_area():
    coord_list = []
    print('Please enter four coordinates (x,y,z) of the parallelogram: ')
    for i in range(0,4):
        coord_list.append(input().strip('()').split(','))
    new = []
    for item in coord_list:
        for num in item:
            new.append(eval('/'.join(map(str,map(float,num.split("/"))))))
    AB_comp = [new[3]-new[0],new[4]-new[1],new[5]-new[2]]
    AC_comp = [new[6]-new[0],new[7]-new[1],new[8]-new[2]]
    CD_comp = [new[9]-new[6],new[10]-new[7],new[11]-new[8]]
    AD_comp = [new[9]-new[0],new[10]-new[1],new[11]-new[2]]
    BC_comp = [new[6]-new[3],new[7]-new[4],new[8]-new[5]]
    BD_comp = [new[9]-new[3],new[10]-new[4],new[11]-new[5]]
    
    if parallelogram_checker(AB_comp,CD_comp,BD_comp,AC_comp):
        i = BC_comp[2]*AB_comp[1] - BC_comp[1]*AB_comp[2]
        j = BC_comp[0]*AB_comp[2] - BC_comp[2]*AB_comp[0]
        k = BC_comp[1]*AB_comp[0] - BC_comp[0]*AB_comp[1]
        area = abs(math.sqrt(i**2+j**2+k**2))
        print('Calculating...')
        time.sleep(3)
        return 'The area of your parallelogram is {} units\u00b2.'.format(round(area,2))
    elif parallelogram_checker(AB_comp,CD_comp,BC_comp,AD_comp):
        i = BD_comp[2]*AB_comp[1] - BD_comp[1]*AB_comp[2]
        j = BD_comp[0]*AB_comp[2] - BD_comp[2]*AB_comp[0]
        k = BD_comp[1]*AB_comp[0] - BD_comp[0]*AB_comp[1]
        area = abs(math.sqrt(i**2+j**2+k**2))
        print('Calculating...')
        time.sleep(3)
        return 'The area of your parallelogram is {} units\u00b2.'.format(round(area,2))
    else:
        return 'The coordinates you entered do not form a parallelogram in the 3D axis.'
    
def triangle_area():
    coord_list = []
    print('Please enter three coordinates (x,y,z) of the triangle: ')
    for i in range(0,3):
        coord_list.append(input().strip('()').split(','))
    new = []
    for item in coord_list:
        for num in item:
            new.append(eval('/'.join(map(str,map(float,num.split("/"))))))
    PQ_comp = [new[3]-new[0],new[4]-new[1],new[5]-new[2]]
    PR_comp = [new[6]-new[0],new[7]-new[1],new[8]-new[2]]
    
    i = PR_comp[2]*PQ_comp[1] - PR_comp[1]*PQ_comp[2]
    j = PR_comp[0]*PQ_comp[2] - PR_comp[2]*PQ_comp[0]
    k = PR_comp[1]*PQ_comp[0] - PR_comp[0]*PQ_comp[1]
    area = abs(math.sqrt(i**2+j**2+k**2)) / 2
    
    print('Calculating...')
    time.sleep(3)
    return 'The area of your triangle is {} units\u00b2.'.format(round(area,2))

def parallelepiped_volume():
    coord_list = []
    print('Please enter the three component form vectors <i,j,k> of the parallelepiped: ')
    for i in range(0,3):
        coord_list.append(input().strip('<>').split(','))
    new = []
    for item in coord_list:
        for num in item:
            new.append(eval('/'.join(map(str,map(float,num.split("/"))))))
    det_a = new[0]*new[4]*new[8] + new[1]*new[5]*new[6] + new[2]*new[3]*new[7]
    det_b = new[1]*new[3]*new[8] + new[0]*new[5]*new[7] + new[2]*new[4]*new[6]
    area = abs(det_a - det_b)
    print('Calculating...')
    time.sleep(3)
    return 'The volume of your parallelpiped is {} units\u00b3.'.format(area)

def anglebwtwovectors():
    a = []
    print('Please enter two vectors to find the angle between the two: ')
    b = input().strip('<>').split(',')
    c = input().strip('<>').split(',')
    d = []
    for item in b:
        a.append(eval('/'.join(map(str,map(float,item.split("/"))))))
    mag_a = round(math.sqrt(a[0]**2+a[1]**2+a[2]**2),2)
    for item in c:
        d.append(eval('/'.join(map(str,map(float,item.split("/"))))))
    mag_d = round(math.sqrt(d[0]**2+d[1]**2+d[2]**2),2)
    e = []
    for i,item in enumerate(d):
        item *= a[i]
        e.append(item)
    dot_product = sum(e)
    if not (dot_product == 0 and mag_a*mag_d == 0):
        if (dot_product / (mag_a*mag_d)) > 1:
            costheta = round(dot_product/(mag_a*mag_d))
        else:
            costheta = round(dot_product/(mag_a*mag_d),2)
        degrees = round(math.degrees(math.acos(costheta)),2)

        print('Calculating...')
        time.sleep(3)
        print('Angle = ' +str(degrees)+u'\N{DEGREE SIGN}')
        if degrees == 90:
            print('These are orthogonal / perpendicular vectors.')
        elif degrees == 0:
            print('These are parallel vectors.')
    else:
        print('It is impossible to find an angle between these two vectors.')

def lineequation3D():
    a = []
    print('Please enter two coordinates of the line: ')
    b = input().strip('()').split(',')
    c = input().strip('()').split(',')
    d = []
    e = []
    for item in b:
        d.append(eval('/'.join(map(str,map(float,item.split("/"))))))
    for item in c:
        e.append(eval('/'.join(map(str,map(float,item.split("/"))))))    
    for i in range(len(b)):
        a.append(e[i]-d[i])
    f = []
    for item in d:
        f.append(-item)
    g = []
    if f[0] > 0:
        g.append('(x+{}) / {}'.format(round(f[0],1),round(a[0],1)))
    elif f[0] == 0:
        g.append('x/{}'.format(round(a[1],1)))   
    else:
        g.append('(x{}) / {}'.format(round(f[0],1),round(a[0],1)))  
        
    if f[1] > 0:
        g.append('(y+{}) / {}'.format(round(f[1],1),round(a[1],1)))
    elif f[1] == 0:
        g.append('y/{}'.format(round(a[1],1)))   
    else:
        g.append('(y{}) / {}'.format(round(f[1],1),round(a[1],1)))  
    
    if f[2] > 0:
        g.append('(z+{}) / {}'.format(round(f[2],1),round(a[2],1)))
    elif f[2] == 0:
        g.append('z/{}'.format(round(a[2],1)))   
    else:
        g.append('(z{}) / {}'.format(round(f[2],1),round(a[2],1)))  
    
    print('Calculating...')
    time.sleep(3)
    print('A possible symmetric equation of the line in the 3D axis is: ')
    print(' = '.join(g))


def planeequation3D():
    coord_list = []
    print('Please enter three coordinates located on the plane: ')
    for i in range(0,3):
        coord_list.append(input().strip('()').split(','))
    new = []
    for item in coord_list:
        for num in item:
            new.append(eval('/'.join(map(str,map(float,num.split("/"))))))
    
    PQ_comp = [new[3]-new[0],new[4]-new[1],new[5]-new[2]]
    PR_comp = [new[6]-new[0],new[7]-new[1],new[8]-new[2]]
    
    i = round(PR_comp[2]*PQ_comp[1] - PR_comp[1]*PQ_comp[2],1)
    j = round(PR_comp[0]*PQ_comp[2] - PR_comp[2]*PQ_comp[0],1)
    k = round(PR_comp[1]*PQ_comp[0] - PR_comp[0]*PQ_comp[1],1)
    
    f = []

    if i < -1:
        f.append(' -'+str(-i)+'x')
    elif i == 1:
        f.append('x')
    elif i == -1:
        f.append('-x')
    elif i == 0:
        f.append('')
    else:
        f.append(str(i)+'x')
    
    if j < -1:
        f.append(' - '+str(-j)+'y')
    elif j == 1:
        f.append('y')
    elif j == -1:
        f.append('- y')
    elif j == 0:
        f.append('')
    else:
        f.append(' + '+str(j)+'y')
    
    if k < -1:
        f.append(' - '+str(-k)+'z')
    elif k == 1:
        f.append('z')
    elif k == -1:
        f.append('- z')
    elif k == 0:
        f.append('')
    else:
        f.append(' + '+str(k)+'z')
    
    d = round(i*(-round(new[0],1))+j*(-round(new[1],1))+k*(-round(new[2],1)),1)
    
    print('Calculating...')
    time.sleep(3)
    print('The general equation of the plane is: ')
    
    if d < 0:
        print(''.join(f) + ' - ' + str(-d) + ' = 0')
    else:
        print(''.join(f) + ' + ' + str(d) + ' = 0')

def anglebwtwoplanes():
    a = []
    print("Please enter the normal vectors of the plane's general equations: <a,b,c>")
    b = input().strip('<>').split(',')
    c = input().strip('<>').split(',')
    d = []
    for item in b:
        a.append(eval('/'.join(map(str,map(float,item.split("/"))))))
    n1 = round(math.sqrt(a[0]**2+a[1]**2+a[2]**2),2)
    for item in c:
        d.append(eval('/'.join(map(str,map(float,item.split("/"))))))
    n2 = round(math.sqrt(d[0]**2+d[1]**2+d[2]**2),2)
    e = []
    for i,item in enumerate(d):
        item *= a[i]
        e.append(item)
    dot_product = abs(sum(e))
    if not (dot_product == 0 and (n1*n2) == 0):
        if (dot_product / (n1*n2)) > 1:
            costheta = round(dot_product/(n1*n2))
        else:
            costheta = round(dot_product/(n1*n2),2)
        degrees = round(math.degrees(math.acos(costheta)),2)
        print('Calculating...')
        time.sleep(3)
        print('Angle = ' +str(degrees)+u'\N{DEGREE SIGN}')
        if degrees == 90:
            print('These are orthogonal / perpendicular planes.')
        elif degrees == 0:
            print('These are parallel planes.')
    else:
        print('These planes do not intersect. ')

def distancebwptandplane():
    P = []
    print('Please enter the coordinate of a point: (x,y,z)')
    b = input().strip('()').split(',')
    print("Please enter the coefficients of the plane's general equation: <a,b,c>")
    c = input().strip('<>').split(',')
    print("Please enter the constant term (d) of the plane's general equation: d")
    d = float(input())
    
    n = []
    for item in b:
        P.append(eval('/'.join(map(str,map(float,item.split("/"))))))
    for item in c:
        n.append(eval('/'.join(map(str,map(float,item.split("/"))))))
    mag_n = round(math.sqrt(n[0]**2+n[1]**2+n[2]**2),2)
    
    
    Q = [-d/n[0],0,0]
    vectorPQ = []
    for i in range(0,3):
        vectorPQ.append(Q[i]-P[i])
        
    e = []
    for i,item in enumerate(n):
        item *= vectorPQ[i]
        e.append(item)
    
    dot_product = abs(sum(e))
    distance = round(dot_product / mag_n,2)
    
    print('Calculating...')
    time.sleep(3)
    print('The distance between the point and the plane is: {} units'.format(distance))

def main():
    print('3D axis calculator:')
    print()
    print('Loading...')
    time.sleep(1)
    print('What would you like to calculate?: ')
    print('\t→ 1. Area of a parallelogram in the 3D axis')
    print('\t→ 2. Area of a triangle in the 3D axis')
    print('\t→ 3. Volume of a parallelepiped')
    print('\t→ 4. Angle between two vectors')
    print('\t→ 5. Equation of line in the 3D axis')
    print('\t→ 6. Equation of plane in the 3D axis')
    print('\t→ 7. Angle between two planes')
    print('\t→ 8. Distance from a point to a plane')
    print() 
    while True:
        try:
            print()
            print('Please select an option or enter STOP if you would like to stop the process: ')
            option = input()
            if option == '1':
                print()
                print(parallelogram_area())
            elif option == '2':
                print()
                print(triangle_area())
            elif option == '3':
                print()
                print(parallelepiped_volume())
            elif option == '4':
                print()
                anglebwtwovectors()
            elif option == '5':
                print()
                lineequation3D()
            elif option == '6':
                print()
                planeequation3D()
            elif option == '7':
                print()
                anglebwtwoplanes()
            elif option == '8':
                print()
                distancebwptandplane()
            elif option == 'STOP':
                print('Thank you for using the 3D Axis Calculator!')
                break
        except:
            print('Your input is invalid. Please enter another.')


main()
