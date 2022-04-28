
from tkinter.tix import TList
import avl_skeleton
import random

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
# print(tlist.retrieve(4))


def chksize(lst):
    if not lst.isRealNode():
        return lst.getSize()
    sz = chksize(lst.getRight())+chksize(lst.getLeft()) + 2
    hi = max(lst.getRight().getHeight(),lst.getLeft().getHeight()) + 1
    if sz != lst.getSize():
        print(" oi "+ str(lst.getValue()))
    if hi != lst.getHeight():
        print(" vey "+ str(tlist.treeRank(lst))+" "+ str(lst.getValue()))
    return sz



random.random()
for i in range(6,71):
    r = int(random.random()*(i-1))
    print(tlist.insert(r ,r))
    lst = tlist.listToArray()
    if (lst[r] != lst[r]):
         print(" oi "+ str(i))
    print(str(r) + "- " + str(tlist.listToArray()))
    #chksize(tlist.getRoot())
for i in range(1,71):
    r = int(random.random()*(70-i))
    print(tlist.delete(r))
    print(tlist.length)
    lst = tlist.listToArray()
    if (lst[r] != lst[r]):
         print(" oi "+ str(i))
    print(str(r) + "- " + str(tlist.listToArray()))
    chksize(tlist.getRoot())

lst = tlist.listToArray()
# for i in range(6,1000):
#     if (lst[i] <= lst[i-1]):
#         print(" oi "+ str(i))
print(tlist.listToArray())
print("fin")

