
from re import A
from tkinter.tix import TList
import avl_skeleton
import random

tlist = avl_skeleton.AVLTreeList()
tlist.insert(0,1)
tlist.insert(1,2)
tlist.insert(2,2)
tlist.insert(3,4)
tlist.insert(4,5)
print(tlist.search(5))
print('fin')

# print(tlist.retrieve(4))


# def chksize(lst):
#     if not lst.isRealNode():
#         return lst.getSize()
#     sz = chksize(lst.getRight())+chksize(lst.getLeft()) + 2
#     hi = max(lst.getRight().getHeight(),lst.getLeft().getHeight()) + 1
#     if sz != lst.getSize():
#         print(" oi "+ str(lst.getValue()))
#     if hi != lst.getHeight():
#         print(" vey "+ str(tlist.treeRank(lst))+" "+ str(lst.getValue()))
#     return sz
#
#
#
# random.random()
# for i in range(6,11):
#     r = int(random.random()*(i-1))
#     print(tlist.insert(r ,r))
#     # lst = tlist.listToArray()
#     # if (lst[r] != lst[r]):
#         #  print(" oi "+ str(i))
#     # print(str(r) + "- " + str(tlist.listToArray()))
#     #chksize(tlist.getRoot())
# # for i in range(1,1001):
#     # r = int(random.random()*(1000-i))
#     # print(tlist.delete(r))
#     # print(tlist.length)
#     # lst = tlist.listToArray()
#     # if (lst[r] != lst[r]):
#         #  print(" oi "+ str(i))
#     # print(str(r) + "- " + str(tlist.listToArray()))
#     # chksize(tlist.getRoot())
#
# # lst2 = avl_skeleton.AVLTreeList()
# # for i in range(0,21):
# #     r = int(random.random()*(i))
# #     print(lst2.insert(r ,r))
# print(tlist.listToArray())
# spl = tlist.split(7)
# print(str(spl[0].listToArray())+ " " + str(spl[2].listToArray()))
# # print()
# # print(lst2.listToArray())
# # print(tlist.concat(lst2))
# # print(tlist.listToArray())
# # # for i in range(6,1000):
# # #     if (lst[i] <= lst[i-1]):
# # #         print(" oi "+ str(i))
# # print(tlist.listToArray())
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
# print("fin")

