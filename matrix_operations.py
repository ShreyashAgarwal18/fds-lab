def a1(mat1, mat2, r1, c1, r2, c2):  #addition of matrix
    finmat = []
    if(r1==r2 and c1==c2):
        for i in range(r1):
            secmat = []
            for j in range(c1):
                c = mat1[i][j] + mat2[i][j]
                secmat.append(c)
            finmat.append(secmat)

    return finmat



def a2(mat1, mat2, r1, c1, r2, c2):   #subtraction of matrix
    finmat = []
    if(r1==r2 and c1==c2):
        for i in range(r1):
            secmat = []
            for j in range(c1):
                c = mat1[i][j] - mat2[i][j]
                secmat.append(c)
            finmat.append(secmat)

    return finmat

def a3(mat1, mat2, r1, c1, r2, c2):   #multiplication of matrix
    finmat = []
    for i in range(len(mat1)):
        secmat = []
        for j in range(len (mat2[0])):
            output = 0
            for k in range(len(mat2)):
                output += mat1[i][k] * mat2[k][j]
            secmat.append(output)
        finmat.append(secmat)
    return finmat

def a4(mat, r, c):  #diagonal sum
    finmat = 0
    for i in range(r):
        finmat += mat[i][i]

    return finmat

def a5(mat, r, c):   #check upper triangular matrix
    finmat = ("Not")
    if r!=c:
        finmat = ("Not")
    else:
        for i in range(r):
            for j in range(c):
                if(i>j and mat[i][j]==0):
                    finmat = ("Yes")
                else:
                    finmat = ("Not")
                    break
            
    return finmat

def a6(mat, r, c):  #transpose
    finmat = []
    j=0
    for i in range(c):
        secmat = []
        for k in range(r):
            secmat.append(mat[k][i])
        j+=1
        finmat.append(secmat)
    return finmat

def findSaddlePoint(mat1, n):   #to find saddle point
    for i in range(n):
        min_row = mat1[i][0]
        col_ind = 0
        for j in range(1, n):
            if (min_row > mat1[i][j]):
                min_row = mat1[i][j]
                col_ind = j
        k = 0
        for k in range(n):
            if (min_row < mat1[k][col_ind]):
                break
            k += 1
        if (k == n):
            print("Value of Saddle Point ", 
                  min_row)
            return True
    return False

def magic(mat1) :   #for magic square
  n = len(mat1)
  sumd1=0
  sumd2=0
  for i in range(n):
    sumd1+=mat1[i][i]
    sumd2+=mat1[i][n-i-1]
  if (sumd1!=sumd2):
    return False
  for i in range(n):
    sumr=0
    sumc=0
    for j in range(n):
      sumr+=mat1[i][j]
      sumc+=mat1[j][i]
    if not(sumr==sumc==sumd1):
      return False
  return True

    
def display(mat):
    if isinstance(mat,list):
        for i in mat:
            for j in i:
                print(j,end=" ")
            print()
    else:
        for i in mat:
            print(mat[i])
                
            
r = int(input("enter the rows: "))
c = int(input("enter the columns: "))

matrix1= []
matrix2 = []

    # matrix=[[1,2,3],[4,5,6],[7,8,9]]
# matrix2=[[1,2,3],[4,5,6],[7,8,9]]
# m,n,m2,n2 = 3,3,3,3

for i in range(0,r):
    temp = []
    for j in range(0,c):
        a = int(input(f'Enter the ${j+1}element of the row ${i+1}: '))
        temp.append(a)
    matrix1.append(temp)
        
        
menu = "Enter One of the operation to apply:\n \
    1. Add\n \
    2. Subtract\n \
    3. Multiply\n \
    4. Diagonal Sum\n \
    5. Check Upper Triangular\n \
    6. Transpose\n \
    7. Saddle point\n\
    8. magic square\n"
    
    
print(menu)
option = int(input("enter the option: "))

if option==1:
    r2 = int(input("enter the number of rows: "))
    c2 = int(input("enter the no. of columns: "))
    for i in range(0,r2):
        temp=[]
        for j in range(0,c2):
            a = int(input(f'ENter the ${j+1} element of the row ${i+1}: '))
            temp.append(a)
        matrix2.append(temp)
    display(a1(matrix1,matrix2,r,c,r2,c2))
   
    
    
elif option==2:
    r2=int(input("enter the no. of rows: "))
    c2=int(input("enter the no. of columns: "))
    for i in range(0,r2):
        temp=[]
        for j in range(0,c2):
            a = int(input(f'enter the ${j+1} element of the row${i+1}: '))
            temp.append(a)
        matrix2.append(temp)
    display(a2(matrix1,matrix2,r,c,r2,c2))

elif option==3:
    r2= int(input("Enter rows: "))
    c2= int(input("Enter columns: "))
    for i in range(0,r2):
        temp = []
        for j in range(0,c2):
            a = int(input(f'enter the ${j+1} element of the row${i+1}: '))
            temp.append(a)
        matrix2.append(temp)
    display(a3(matrix1,matrix2,r,c,r2,c2))

elif option == 4:
    print(a4(matrix1,r,c))

elif option == 5:
    display(a5(matrix1,r,c))

elif option == 6:
    print(a6(matrix1,r,c))
    
elif option == 7:
    findSaddlePoint(matrix1,len(matrix1))
        
elif option == 8:
    if(magic(matrix1)==1):
     print("Matrix 1 is a magic square.")
    else:
     print("Matrix 1 is not a magic square.")
    




    
    
    
            
        
        

        




        
        
    
