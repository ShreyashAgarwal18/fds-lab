def addPolynomial(p1,p2,n1,n2):
    c1 =0
    c2=0
    p3=[]
    while(c1<n1 and c2<n2):
        if p1[c1][1] == p2[c2][1]:
            c0 = p1[c1][0]+p2[c2][0]
            exp = p1[c1][1]
            p3.append([c0,exp])
            c1+=1
            c2+=1
        elif p2[c2][1] > p1[c1][1]:
            p3.append([p2[c2][0],p2[c2][1]])
            c1+=1
        elif p1[c1][1] > p2[c2][1]:
            p3.append([p1[c1][0],p1[c1][1]])
            c2+=1
    while c1<n1:
        p3.append([p1[c1][0],p1[c1][1]])
        c1+=1
    while c2<n2:
        p3.append([p2[c2][0],p2[c2][1]])
        c2+=1
    return p3

def multiplyPolynomial(p1,p2,n1,n2):
    ret=[]
    p3 = [0]*(n1+n2-1)
    for i in range(0,n1):
        for j in range(0,n2):
            p3[p1[i][1]+p2[j][1]] += p1[i][0]*p2[j][0]
    for ind,val in enumerate(p3):
        ret.append([val,ind])
        
    del(p3)
    return ret

def evalPolynomial(p1,n1):
    x = int(input("Enter the value of x: "))
    sum = 0
    for i in range(n1):
        sum+= p1[i][0]*(x**p1[i][1])
    return sum

def inputPolynomial():
    n = int(input("Enter the number of non-zero terms in the polynomial: "))
    polynomial = []
    for _ in range(n):
        coefficient = int(input("Enter the coefficient: "))
        exponent = int(input("Enter the exponent: "))
        polynomial.append([coefficient, exponent])
    return polynomial,n

[p1,n1] = inputPolynomial()
[p2,n2] = inputPolynomial()

menu = "Enter one of the following option: \n \
1. Add\n \
2. Multiply\n \
3. Evaluate Polynomial 1\n \
4. Evaluate Polynomial 2"
print(menu)
print()
option = int(input("Enter the option: "))

if option==1:
    if n1>n2:
        print(addPolynomial(p1,p2,n1,n2))
    else:
        print(addPolynomial(p2,p1,n2,n1))
elif option==2:
    print(multiplyPolynomial(p1,p2,n1,n2))
elif option==3:
    print(evalPolynomial(p1,n1))
elif option==4:
    print(evalPolynomial(p2,n2))