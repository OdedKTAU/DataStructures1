import csv
import time
import avl_skeleton
import math
import random
from re import A
from tkinter.tix import TList
import avl_skeleton
import random


def Q2(n):
    le = int(1000*(2**n))
    sol = []
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
    s2 = lst2.split(le - 1)
    sol.append(s1[4])
    sol.append(s1[3])
    sol.append(s2[4])
    sol.append(s2[3])
    
    t1 = time.time_ns()
    sol.append(t1-t0)

    lst = avl_skeleton.AVLTreeList()
    for i in range(le):
        r = int(random.random()*(i))
        lst.insert(r ,r)
    t0 = time.time_ns()
    for i in range(1, le):
        r = int(random.random()*(le - i))
        lst.delete(r)
    t1 = time.time_ns()
    sol.append(t1-t0)

    lst = avl_skeleton.AVLTreeList()
    for i in range(int(le/2)):
        r = int(random.random()*(i))
        lst.insert(r ,r)
    t0 = time.time_ns()
    for i in range(int(le / 4)):
        r = int(random.random()*(i))
        lst.insert(r ,r)
        i+=1
        r = int(random.random()*(le/4 - i))
        lst.delete(r)   
    t1 = time.time_ns()
    sol.append(t1-t0)

    return sol










tlist = avl_skeleton.AVLTreeList()
print(str(tlist.insert(0,1)))
print(avl_skeleton.AVLTreeList.getMax(tlist.getRoot()).getValue())
print(tlist.insert(1,2))
print(avl_skeleton.AVLTreeList.getMax(tlist.getRoot()).getValue())
print(tlist.getRoot().right.getValue())
print(tlist.insert(2,3))
print(tlist.getRoot().left.getValue())
print(tlist.retrieve(1))
print(tlist.insert(3,4))
print(tlist.retrieve(2))
print(tlist.insert(2,5))
print(tlist.insert(3,6))
print(tlist.retrieve(4))
tlist2 = avl_skeleton.AVLTreeList()


def chksize(lst):
    if not lst.isRealNode():
        if -1 != lst.getSize():
            print(" oi NotReal "+ str(lst.getValue()) + " " + str(lst.getSize()))
        if -1 != lst.getHeight():
            print(" oi NotReal "+ str(lst.getValue()) + " " + str(lst.getHeight()))
        return -1
    sz = chksize(lst.getRight())+chksize(lst.getLeft()) + 2
    hi = max(lst.getRight().getHeight(),lst.getLeft().getHeight()) + 1
    if sz != lst.getSize():
        print(" oi "+ str(tlist.treeRank(lst))+" "+ str(lst.getValue()) + " " + str(lst.getSize() - sz)+ " " + str(lst.getSize())+" " + str(sz))
    if hi != lst.getHeight():
        print(" vey "+ str(tlist.treeRank(lst))+" "+ str(lst.getValue()))
    if (lst.getRight().getHeight() - lst.getLeft().getHeight()) not in [-1,0,1]:
        print(" oof "+ str(tlist.treeRank(lst))+" "+ str(lst.getValue()) + " " + str(lst.getRight().getHeight() - lst.getLeft().getHeight()))
    return sz



random.random()
for i in range(6,20001):
    r = int(random.random()*(i-1))
    tlist.insert(r ,r)
r2 = int(random.random()*(20000))
for i in range(0,r2):
    r = int(random.random()*(i-1))
    tlist2.insert(r ,r)
print(tlist.listToArray())
print("res-" + str(tlist.search(10)))
    # lst = tlist.listToArray()
    # if (lst[r] != lst[r]):
        #  print(" oi "+ str(i))
    # print(str(r) + "- " + str(tlist.listToArray()))
    #chksize(tlist.getRoot())
# # for i in range(1,1001):
#     # r = int(random.random()*(1000-i))
#     # print(tlist.delete(r))
#     # print(tlist.length)
#     # lst = tlist.listToArray()
#     # if (lst[r] != lst[r]):
#         #  print(" oi "+ str(i))
#     # print(str(r) + "- " + str(tlist.listToArray()))
#     # chksize(tlist.getRoot())

# # lst2 = avl_skeleton.AVLTreeList()
# # for i in range(0,21):
# #     r = int(random.random()*(i))
# #     print(lst2.insert(r ,r))

# tlist.concat(tlist2)
chksize(tlist.getRoot())
# print(tlist.listToArray())
r = int(random.random()*tlist.length)
spl = tlist.split(r)
print(str(spl[0].listToArray())+ " " + str(spl[2].listToArray()))
t1 =  chksize(spl[0].getRoot())
print("****")
t2 = chksize(spl[2].getRoot())
print(t1 - t2)


# # print()
# # print(lst2.listToArray())
# # print(tlist.concat(lst2))
# # print(tlist.listToArray())
# # # for i in range(6,1000):
# # #     if (lst[i] <= lst[i-1]):
# # #         print(" oi "+ str(i))
# print(tlist.listToArray())
# # for i in range(30,1001):
# #     r = int(random.random()*(i-1))
# #     print(tlist.insert(r ,r))
# #     lst = tlist.listToArray()
# #     if (lst[r] != lst[r]):
# #          print(" oi "+ str(i))
# #     print(str(r) + "- " + str(tlist.listToArray()))
# #     chksize(tlist.getRoot())
# # for i in range(1,1001):
# #     r = int(random.random()*(1000-i))
# #     print(tlist.delete(r))
# #     print(tlist.length)
# #     lst = tlist.listToArray()
# #     if (lst[r] != lst[r]):
# #          print(" oi "+ str(i))
# #     print(str(r) + "- " + str(tlist.listToArray()))
# #     chksize(tlist.getRoot())
print("fin")

