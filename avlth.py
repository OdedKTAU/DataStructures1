import csv
import time
import avl_skeleton
import math
import random

def Q1(n):
    le = int(1000*(2**n))
    sol = [n]
    lst = avl_skeleton.AVLTreeList()
    cnt = 0
    tot = 0

    t0 = time.time_ns()
    for i in range(le):
        r = int(random.random()*(i))
        tot += lst.insert(r ,r)
        cnt += 1
    t1 = time.time_ns()
    sol.append(tot)

    lst = avl_skeleton.AVLTreeList()
    tot = 0
    cnt = 0
    for i in range(le):
        r = int(random.random()*(i))
        lst.insert(r ,r)
    t0 = time.time_ns()
    for i in range(1, le):
        r = int(random.random()*(le - i))
        tot += lst.delete(r)
        cnt += 1
    t1 = time.time_ns()
    sol.append(tot)

    tot = 0
    cnt = 0
    lst = avl_skeleton.AVLTreeList()
    for i in range(int(le/2)):
        r = int(random.random()*(i))
        lst.insert(r ,r)
    t0 = time.time_ns()
    for i in range(int(le / 4)):
        r = int(random.random()*(i))
        tot += lst.insert(r ,r)
        cnt += 1
        i+=1
        r = int(random.random()*(le/4 - i))
        tot += lst.delete(r)
        cnt += 1
    t1 = time.time_ns()
    sol.append(tot)

    return sol


def Q2(n):
    le = int(1000*(2**n))
    sol = [n]
    lst1 = avl_skeleton.AVLTreeList()
    lst2 = avl_skeleton.AVLTreeList()

    for i in range(le):
        r = int(random.random()*(i))
        lst1.insert(r ,r)
    for i in range(le):
        r = int(random.random()*(i))
        lst2.insert(r ,r)

    s = int(random.random()*le - 1)
    s1 = lst1.split(s)
    s = avl_skeleton.AVLTreeList.treeRank(lst2.getRoot())
    if s >0:
        s -= 1
    s2 = lst2.split(s)
    sol.append(s1[4])
    sol.append(s1[3])
    sol.append(s2[4])
    sol.append(s2[3])
    
    return sol

def Q3(n):
    le = int(1000*(2**n))
    sol = [n]
    lst = avl_skeleton.AVLTreeList()
    cnt = 0
    tot = 0

    t0 = time.time_ns()
    for i in range(le):
        r = int(random.random()*(i))
        tot += lst.insert(r ,r)
        cnt += 1
    t1 = time.time_ns()
    sol.append(tot)

    lst = avl_skeleton.AVLTreeList()
    tot = 0
    cnt = 0
    for i in range(le):
        r = int(random.random()*(i))
        lst.insert(r ,r)
    t0 = time.time_ns()
    for i in range(1, le):
        r = int(random.random()*(le - i))
        tot += lst.delete(r)
        cnt += 1
    t1 = time.time_ns()
    sol.append(tot)

    tot = 0
    cnt = 0
    lst = avl_skeleton.AVLTreeList()
    for i in range(int(le/2)):
        r = int(random.random()*(i))
        lst.insert(r ,r)
    t0 = time.time_ns()
    for i in range(int(le / 4)):
        r = int(random.random()*(i))
        tot += lst.insert(r ,r)
        cnt += 1
        i+=1
        r = int(random.random()*(le/4 - i))
        tot += lst.delete(r)
        cnt += 1
    t1 = time.time_ns()
    sol.append(tot)

    return sol








q2 = [['i', 'Avrage Random', 'Max Random', 'Avrage Last', 'Max Last']]
for i in range(1,11):
    q2.append(Q2(i))
    print(q2)
with open('Q2f.csv', "w") as q2csv:
    wr = csv.writer(q2csv)
    wr.writerows(q2)

