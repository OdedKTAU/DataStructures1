
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
print(tlist.insert(4,5))
print(tlist.retrieve(4))
for i in range(6,1001):
    
    tlist.insert(5 ,i)
#    print(tlist.listToArray())
lst = tlist.listToArray()
for i in range(6,1000):
    if (lst[i] >= lst[i-1]):
        print(" oi "+i)

print("fin")