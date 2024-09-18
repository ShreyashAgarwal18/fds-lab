def union(s1,s2):
    unionSet = s2.copy()
    for i in s1:
        if i not in s2:
            unionSet.append(i)
    return unionSet

def union3(s1,s2,s3):
    unionSet = s2.copy() or []
    for i in s1:
        if i not in s2:
            unionSet.append(i)
    for i in s3:
        if i not in unionSet:
            unionSet.append(i)
    return unionSet

def intersection(s1,s2):
    ret=[]
    for i in s1:
      if i in s2:
            ret.append(i)
    return ret

def intersection3(s1,s2,s3):
    ret = []
    for i in s1:
        if i in s2 and i in s3:
            ret.append(i)
    return ret

def q1(s1,s2):
    ret = []
    for i in s2:
        if i in s1:
            ret.append(i)
    return ret

def q2(s1,s2):
    ret = []
    inter = q1(s1,s2)
    uni = union(s1,s2)
    for i in uni:
        if i in inter:
            continue
        else:
            ret.append(i)
    return ret 

def q3(s1,s2,n):
    
    uni2 = union(s1,s2)
    return n-len(uni2)

def q4(s1,s2,s3):
    inter3 = intersection3(s1,s2,s3)
    inter2 = intersection(s1,s3)
    return len(inter2)-len(inter3)

def q5(s1,s2,s3,n):
    uni3 = union3(s1,s2,s3)
    return n-len(uni3)

def q6(s1,s2,s3):
    return union3(s1,s2,s3)

def q7(s1,s2,s3):
    return intersection3(s1,s2,s3)


# t = int(input("Enter the no of test cases"))
# while(t):
nT = int(input("Enter the total number of students: "))
input_str_a = input("Enter elements of the cricket")
a = input_str_a.split()
a = [int(num) for num in a]
input_str_b = input("Enter elements of badminton: ")
b = input_str_b.split()
b = [int(num) for num in b]
input_str_c = input("Enter elements of the Football")
c = input_str_c.split()
c = [int(num) for num in c]
print("i) ", q1(a,b))
print("ii) ", q2(a,b))
print("iii) ", q3(a,b,nT))
print("iv) ", q4(a,b,c))
print("v) ", q5(a,b,c,nT))
print("vi) ", q6(a,b,c))
print("vii) ", q7(a,b,c))
#    t=t-1

