
from tkinter.tix import TList
import avl_skeleton

tlist = avl_skeleton.AVLTreeList()
print(str(tlist.insert(0,1)))
print(avl_skeleton.AVLTreeList.getMax(tlist.getRoot()).getValue())
print(tlist.insert(1,2))
print(avl_skeleton.AVLTreeList.getMax(tlist.getRoot()).getValue())
print(tlist.getRoot().right.getValue())
print(tlist.insert(2,3))
print(tlist.getRoot().left.getValue())
print(tlist.retrieve(3))
print("fin")