# username - complete info
# id1      - complete info
# name1    - complete info
# id2      - complete info
# name2    - complete info
# TODO: Split


"""A class represnting a node in an AVL tree"""





from hashlib import new
from ntpath import join
from tkinter.tix import TList
from turtle import left, right


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

	@type value: str
	@param value: data of your node
	"""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1
        self.size = -1

    """returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	"""

    def getLeft(self):
        return self.left

    """returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	"""

    def getRight(self):
        return self.right


    """returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""

    def getParent(self):
        return self.parent

    """return the value

	@rtype: str
	@returns: the value of self, None if the node is virtual
	"""

    def getValue(self):
        return self.value

    """returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""

    def getHeight(self):
        return self.height

    """returns the size

		@rtype: int
		@returns: the size of self, -1 if the node is virtual
		"""

    def getSize(self):
        return self.size

    """sets left child

	@type node: AVLNode
	@param node: a node
	"""

    def setLeft(self, node):
        self.left = node

    """sets right child

	@type node: AVLNode
	@param node: a node
	"""

    def setRight(self, node):
        self.right = node

    """sets parent

	@type node: AVLNode
	@param node: a node
	"""

    def setParent(self, node):
        self.parent = node

    """sets value

	@type value: str
	@param value: data
	"""

    def setValue(self, value):
        self.value = value

    """sets the balance factor of the node

	@type h: int
	@param h: the height
	"""

    def setHeight(self, h):
        self.height = h

    """sets the size of the node's subtree

		@type s: int
		@param s: the size
		"""

    def setSize(self, s):
        self.size = s

    """returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""

    def isRealNode(self):
        return self.height > -1

    """sets a node as a leaf in the tree
			"""

    def setLeaf(self):
        self.left = AVLNode("")
        self.left.setParent(self)
        self.right = AVLNode("")
        self.right.setParent(self)
        self.parent = AVLNode("")
        self.setHeight(0)
        self.setSize(0)

    """return the Balance Factor of a given node
	@rtype: int
	@returns: height differential of the children nodes
				"""

    def getBalanceFactor(self):
        return self.getLeft().getHeight() - self.getRight().getHeight()

    """sets a node as at left/fight position (or new root)
				@type parent: AVLNode
				@param parent: the current parent node
				@type new_child: AVLNode
				@param node: a node that will be set as a child
				@type current_child: AVLNode
				@param current_child: the current left/right child of the given node
				@pre: self.getLeft() == current_child or self.getRight() == current_child
				"""

    def setProperChild(self, tree_list, new_child, current_child):
        if not self.isRealNode():
            tree_list.setRoot(new_child)

        elif self.getRight() == current_child:
            self.setRight(new_child)

        else:
            self.setLeft(new_child)
        return

    """returns whether self is a leaf in a tree 

		@rtype: bool
		@returns: False if self is not a leaf, True otherwise.
		"""

    def isLeaf(self):
        return self.getParent().isRealNode() and not self.getRight().isRealNode() and not self.getLeft().isRealNode()


"""
A class implementing the ADT list, using an AVL tree.
"""


class AVLTreeList(object):
    """
	Constructor, you are allowed to add more fields.

	"""

    def __init__(self):
        self.root = None
        self.length = 0

    """returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""

    def empty(self):
        return self.root is None

    """retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	"""

    def retrieve(self, i):
        return AVLTreeList.treeSelect(self.root, i).getValue()

    """inserts val at position i in the list

	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

    def insert(self, i, val):
        new_node = AVLNode(val)
        new_node.setLeaf()
        new_parent = None

        if self.length == 0:
            self.root = new_node
            self.length += 1
            return 0

        elif i == self.length:
            new_parent = AVLTreeList.getMaxInsert(self.root)
            new_parent.setRight(new_node)
            #new_parent.setHeight(max(0, new_parent.getLeft().getHeight()) + 1)

        else:
            new_parent = AVLTreeList.treeSelectInsert(self.root, i)
            if not new_parent.getLeft().isRealNode():
                new_parent.setLeft(new_node)
                #new_parent.setHeight(max(0, new_parent.getRight().getHeight()) + 1)

            else:
                new_parent = AVLTreeList.getPrevInsert(new_parent)
                new_parent.setRight(new_node)
                #new_parent.setHeight(max(0, new_parent.getLeft().getHeight()) + 1)

        new_node.setParent(new_parent)
        #AVLTreeList.fixHeight(new_parent)
        rotations_counter = AVLTreeList.BalanceTreeFrom(self, new_parent)
        self.length += 1
        # TODO: Fix heights during rotations, count height changes & add node.size() maintenance
        return rotations_counter

    """deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

    def delete(self, i):
        if self.length == 1:
            self.root = None
            self.length = 0;
        relevant_node = AVLTreeList.treeSelectDel(self.root, i)
        parent = relevant_node.getParent()
        relevant_node.setParent(AVLNode(""))

        # Deleted node has two children
        if relevant_node.getRight().isRealNode() and relevant_node.getLeft().isRealNode():
            # Get successor
            replacement = AVLTreeList.getMinDel(relevant_node.getRight())
            fix_from = replacement.getParent()
            if fix_from == relevant_node:
                fix_from = replacement;


            # Bypass successor's parent to its child
            replacement.getParent().setProperChild(self, replacement.getRight(), replacement)
            replacement.getRight().setParent(replacement.getParent())

            # Replace deleted node with successor
            replacement.setParent(parent)
            replacement.setRight(relevant_node.getRight())
            replacement.setLeft(relevant_node.getLeft())
            parent.setProperChild(self, replacement, relevant_node)

            relevant_node.setLeft(AVLNode(""))
            relevant_node.setRight(AVLNode(""))
            replacement.getRight().setParent(replacement)
            replacement.getLeft().setParent(replacement)
            replacement.setSize(replacement.getLeft().getSize() + replacement.getRight().getSize() + 2)

        else:
            fix_from = parent
            if relevant_node.isLeaf():  # Case 1 - Delete node is a leaf
                parent.setProperChild(self, AVLNode(""), relevant_node)

            elif not relevant_node.getRight().isRealNode():  # Case 2.1 - Deleted node has no right child
                parent.setProperChild(self, relevant_node.getLeft(), relevant_node)
                relevant_node.getLeft().setParent(parent)
                relevant_node.setLeft(AVLNode(""))

            else:  # Case 2.2 - Deleted node has no left child
                parent.setProperChild(self, relevant_node.getRight(), relevant_node)
                relevant_node.getRight().setParent(parent)
                relevant_node.setRight(AVLNode(""))

        #if fix_from.isRealNode():
            #AVLTreeList.adjustHeights(fix_from)
        rotations_counter = AVLTreeList.BalanceTreeFrom(self, fix_from)
        self.length -= 1
        # TODO: Fix heights during rotations, count height changes & add node.size() maintenance
        return rotations_counter

    """returns the value of the first item in the list

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""

    def first(self):
        if self.length() == 0:
            return None
        return AVLTreeList.getMin(self.root).getValue()

    """returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""

    def last(self):
        if self.length() == 0:
            return None
        return AVLTreeList.getMax(self.root).getValue()

    """returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""

    def listToArray(self):
        result = []
        if self.length == 0:
            return result

        stack = []
        current = self.root
        while True:
            if current.isRealNode():
                stack.append(current)
                current = current.getLeft()

            elif stack:
                current = stack.pop()
                result.append(current.getValue())
                current = current.getRight()
            else:
                break
        return result

    """returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""

    def length(self):
        return self.length()

    """splits the list at the i'th index

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list according to whom we split
	@rtype: list
	@returns: a list [left, val, right], where left is an AVLTreeList representing the list until index i-1,
	right is an AVLTreeList representing the list from index i+1, and val is the value at the i'th index.
	"""

    def split(self, i):
        vars = AVLTreeList.treeSelectSplit(self.root, i)
        leftL = vars[0]
        rightL = vars[1]
        snode = vars[2]
        llst = AVLTreeList()
        #if leftL[len(leftL) - 1][0].isRealNode():
        llst.setRoot( leftL[len(leftL) - 1][0])
        llst.length = llst.root.getSize() + 1
        llst.getRoot().setParent(AVLNode(""))
        for i in range(1,len(leftL)):
            tlst = AVLTreeList()
            tlst.setRoot(leftL[len(leftL) - i - 1][1])
            tlst.length = tlst.getRoot().getSize() + 1
            tlst.getRoot().setParent(AVLNode(""))
            nnode = leftL[len(leftL) - i - 1][0]
            nnode.setLeaf()
            llst = AVLTreeList.join(tlst, llst, nnode)
        
        
        rlst = AVLTreeList()
        #if rightL[len(rightL) - 1][0].isRealNode():
        rlst.setRoot( rightL[len(rightL) - 1][0])
        rlst.length = rlst.root.getSize() + 1
        rlst.getRoot().setParent(AVLNode(""))
        for i in range(1,len(rightL)):
            tlst = AVLTreeList()
            tlst.setRoot(rightL[len(rightL) - i - 1][1])
            tlst.length = tlst.getRoot().getSize() + 1
            tlst.getRoot().setParent(AVLNode(""))
            nnode = rightL[len(rightL) - i - 1][0]
            nnode.setLeaf
            rlst = AVLTreeList.join(rlst, tlst, nnode)
            print(str(rlst.listToArray()) + " t t")



        return [llst, snode, rlst]

    """concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""

    def concat(self, lst):
        original_height_diff = self.root.getHeight() - lst.root.getHeight()
        new_root = AVLTreeList.getMax(self.root)
        self.delete(self.length - 1)
        self.join( lst, new_root)
        return original_height_diff


    """concatenates lst2 to lst1 with new_root between them

	@type lst1: AVLTreeList
	@param lst: a list to be concatenated after self
    @type lst2: AVLTreeList
	@param lst2: a list to be concatenated after self
	@rtype: AVLTreeList
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
    
    def join(self, lst2, new_root):
        height_diff = self.root.getHeight() - lst2.root.getHeight()
        new_root.setLeaf()
        if lst2.length == 0:
            if self.length == 0:
                self.setRoot(new_root)
                self.length = 1
                return self
            parent = self.getMaxInsert(self.getRoot())
            parent.setRight(new_root)
            new_root.setParent(parent)
            new_root.setSize(new_root.getRight().getSize() + new_root.getLeft().getSize() + 2)
            self.length += 1
            AVLTreeList.BalanceTreeFrom(self,parent)
            return self
        elif self.length == 0:
            parent = AVLTreeList.treeSelectInsert(lst2.getRoot(), 0)
            parent.setLeft(new_root)
            new_root.setParent(parent)
            lst2.length += 1
            new_root.setSize(new_root.getRight().getSize() + new_root.getLeft().getSize() + 2)
            AVLTreeList.BalanceTreeFrom(lst2, parent)
            self = lst2
            return self


        if height_diff == 0:
            new_root.setLeft(self.root)
            self.root.setParent(new_root)
            new_root.setRight(lst2.root)
            new_root.setSize(new_root.getRight().getSize() + new_root.getLeft().getSize() + 2)
            
            lst2.root.setParent(new_root)
            new_root.setHeight(max(new_root.getLeft().getHeight(), new_root.getRight().getHeight()) + 1)
            self.setRoot(new_root)

        elif height_diff < 0:
            left_height = self.root.getHeight()
            start = lst2.root

            while start.getHeight() > left_height:
                start.setSize(start.getSize() + self.length + 1)
                start = start.getLeft()

            new_root.setParent(start.getParent())
            new_root.getParent().setLeft(new_root)
            new_root.setRight(start)
            start.setParent(new_root)
            new_root.setLeft(self.root)
            self.root.setParent(new_root)
            new_root.setSize(new_root.getLeft().getSize()+new_root.getRight().getSize()+2)
            new_root.setHeight(self.root.getHeight() + 1)

            #AVLTreeList.fixHeight(new_root)
            AVLTreeList.BalanceTreeFrom(self, new_root.getParent())

            self.setRoot(lst2.root)
            lst2.setRoot(None)

        else:
            right_height = lst2.root.getHeight()
            start = self.root

            while start.getHeight() > right_height:
                start.setSize(start.getSize() + lst2.length + 1)
                start = start.getRight()

            new_root.setParent(start.getParent())
            new_root.getParent().setRight(new_root)
            new_root.setLeft(start)
            start.setParent(new_root)
            new_root.setRight(lst2.root)
            lst2.root.setParent(new_root)
            new_root.setSize(new_root.getLeft().getSize()+new_root.getRight().getSize()+2)
            new_root.setHeight(lst2.root.getHeight() + 1)

            #AVLTreeList.fixHeight(new_root)
            AVLTreeList.BalanceTreeFrom(self, new_root.getParent())

            lst2.setRoot(None)

        self.length = lst2.length + self.length + 1
        return self

    """searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""

    def search(self, val):
        return AVLTreeList.inOrderSearch(self.root, val)

    """returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""

    def getRoot(self):
        return self.root

    """set a new root

		@type val: AVLNode
		@param val: The new root to the tree list
		"""

    def setRoot(self, node):
        self.root = node

    """returns the max node of a subtree, starting from it's root

		@rtype: AVLNode
		@returns: the max node in a tree
		"""

    @staticmethod
    def getMax(some_root):
        while some_root.getRight().isRealNode():
            some_root = some_root.getRight()
        return some_root

    """returns the max node of a subtree, starting from it's root, and updating the size for each node it passes

		@rtype: AVLNode
		@returns: the max node in a tree
		"""

    @staticmethod
    def getMaxInsert(some_root):
        some_root.setSize(some_root.getSize()+1)
        while some_root.getRight().isRealNode():
            some_root = some_root.getRight()
            some_root.setSize(some_root.getSize()+1)
        return some_root


    """returns the min node of a subtree, starting from it's root

			@rtype: AVLNode
			@returns: the min node in a tree
			"""

    @staticmethod
    def getMin(some_root):
        while some_root.getLeft().isRealNode():
            some_root = some_root.getLeft()
        return some_root
    
    
    
    
    """returns the min node of a subtree, starting from it's root and deducts 1 from the height of all nodes passed in the branch

			@rtype: AVLNode
			@returns: the min node in a tree
			"""

    @staticmethod
    def getMinDel(some_root):
        some_root.setSize(some_root.getSize() - 1) 
        while some_root.getLeft().isRealNode():
            some_root = some_root.getLeft()
            some_root.setSize(some_root.getSize() - 1) 
        return some_root

    """returns the node at i'th index of the list (which is the node at rank i +1) 

			@pre: 1 <= rank <= self.length()
			@type some_root: AVLNode
			@param some_root: the root to start the search from
			@type rank: int
			@param int: rank of desired node
			@rtype: AVLNode
			@returns: the node at the given rank
			"""

    @staticmethod
    def treeSelect(some_root, rank):
        counter = some_root.getLeft().getSize() + 1
        if rank == counter:
            return some_root

        elif rank < counter:
            return AVLTreeList.treeSelect(some_root.getLeft(), rank)
        else:
            return AVLTreeList.treeSelect(some_root.getRight(), rank - counter - 1)

    """returns the node at i'th index of the list (which is the node at rank i +1) and adjust the sizes of the parent nodes

			@pre: 1 <= rank <= self.length()
			@type some_root: AVLNode
			@param some_root: the root to start the search from
			@type rank: int
			@param int: rank of desired node
			@rtype: AVLNode
			@returns: the node at the given rank
			"""

    @staticmethod
    def treeSelectInsert(some_root, rank):
        counter = some_root.getLeft().getSize() + 1
        some_root.setSize(some_root.getSize() + 1)
        
        if rank == counter:
            return some_root
        elif rank < counter:
            # if (some_root.getLeft().getHeight() >= some_root.getRight().getHeight()):
            #     some_root.setHeight(some_root.getHeight() + 1)
            return AVLTreeList.treeSelectInsert(some_root.getLeft(), rank)
        else:
            # if (some_root.getLeft().getHeight() <= some_root.getRight().getHeight()):
            #     some_root.setHeight(some_root.getHeight() + 1)
            return AVLTreeList.treeSelectInsert(some_root.getRight(), rank - counter - 1)


    """returns a list containing the required methods for a split operation
			@pre: 1 <= rank <= self.length()
			@type some_root: AVLNode
			@param some_root: the root to start the search from
			@type rank: int
			@param int: rank of desired node
			@rtype: List
			@returns: a list [left, right, x] where x is the node at i'th index of the list (which is the node at rank i +1) , and right and left are lists of arrays 
            of size 2 containing the nodes and corresponding trees in the right and left sides of a split of self at x respectively.
			"""

    @staticmethod
    def treeSelectSplit(some_root, rank):

        counter = some_root.getLeft().getSize() + 1
        x = some_root
        left = []
        right = []
        while True:
            if rank == counter:
                x = some_root
                right.append([x.getRight()])
                left.append([x.getLeft()])
                break
            elif rank < counter:
                right.append([some_root, some_root.getRight()])
                some_root = some_root.getLeft()
                counter = some_root.getLeft().getSize() + 1
            else:
                left.append([some_root, some_root.getLeft()])
                rank = rank - counter - 1
                some_root = some_root.getRight()
                counter = some_root.getLeft().getSize() + 1

        return [left, right, x]


    @staticmethod
    def treeSelectDel(some_root, rank):
        counter = some_root.getLeft().getSize() + 1
        some_root.setSize(some_root.getSize() - 1)
        
        if rank == counter:
            return some_root
        elif rank < counter:
            # if (some_root.getLeft().getHeight() >= some_root.getRight().getHeight()):
            #     some_root.setHeight(some_root.getHeight() + 1)
            return AVLTreeList.treeSelectDel(some_root.getLeft(), rank)
        else:
            # if (some_root.getLeft().getHeight() <= some_root.getRight().getHeight()):
            #     some_root.setHeight(some_root.getHeight() + 1)
            return AVLTreeList.treeSelectDel(some_root.getRight(), rank - counter - 1)

    """returns the predecessor of a node in the tree

			@type node: AVLNode
			@param node: node at rank i
			@rtype: AVLNode
			@returns: node at rank i - 1
			"""

    @staticmethod
    def getPrev(node):
        if node.getLeft().isRealNode():
            return AVLTreeList.getMax(node.getLeft())

        while node == node.getParent().getLeft():
            node = node.getParent()
            if node.getParent() is None:
                return None  # i.e. this node is the minimal node of the tree
        return node.getParent()

    """returns the predecessor of a node in the tree and fixes height and sizes

			@type node: AVLNode
			@param node: node at rank i
			@rtype: AVLNode
			@returns: node at rank i - 1
			"""

    @staticmethod
    def getPrevInsert(node):
        if node.getLeft().isRealNode():
            return AVLTreeList.getMaxInsert(node.getLeft())

        while node == node.getParent().getLeft():
            node.setSize(node.getSize()-1)
            node = node.getParent()
            
        if not node.getParent().isRealNode():
            return None  # i.e. this node is the minimal node of the tree
        return node.getParent()


    """returns the successor of a node in the tree

				@type node: AVLNode
				@param node: node at rank i
				@rtype: AVLNode
				@returns: node at rank i + 1
				"""

    @staticmethod
    def getNext(node):
        if node.getRight().isRealNode():
            return AVLTreeList.getMin(node.getRight())

        while node == node.getParent().getRight():
            node = node.getParent()
            if node.getParent() is None:
                return None  # i.e. this node is the maximal node of the tree
        return node.getParent()

    """returns the first index of a given value

				@type node: AVLNode
				@param node: the node to start the walk from
				@type value: string
				@param value: the value to search in the tree nodes
				@rtype: int
				@returns: list index of first appearance of a given value, -1 if value not found
				"""

    @staticmethod
    def inOrderSearch(node, value):
        if node.isRealNode():

            if node.getValue() == value:
                return AVLTreeList.treeRank(node) - 1
            v = AVLTreeList.inOrderSearch(node.getLeft(), value)
            if v >-1:
                return v


            
            return AVLTreeList.inOrderSearch(node.getRight(), value)

        return -1

    """returns the first index of a given value

				@type node: AVLNode
				@param tree: the node to start the walk from
				@rtype: int
				@returns: the rank of a node in its tree
				"""

    @staticmethod
    def treeRank(node):
        counter = node.getLeft().getSize() + 1

        while node.getParent().isRealNode():
            parent = node.getParent()
            if node == parent.getRight():
                counter += parent.getLeft().getSize() + 1
            node = parent

        return counter

    """fix the heights of nodes up a tree

					@type node: AVLNode
					@param tree: the node to start the walk from
					"""

    @staticmethod
    def adjustHeights(node):
        while node.isRealNode():
            node.setHeight(max(node.getRight().getHeight() + 1, node.getLeft().getHeight() + 1))
            node = node.getParent()

    """Balance an AVL tree, starting from the parent of the recently added leaf

						@pre: node.isRealNode() = True
						@type tree_list: AVLTreeList
						@param tree_list: a pointer to the tree list
						@type node: AVLNode
						@param node: the node to start the walk from
						@rtype: int
						@returns: total number of rotations done to balance the tree 
						"""

    @staticmethod
    def BalanceTreeFrom(tree_list, node):
        counter = 0
        while node.isRealNode():
            prev = node.getHeight()
            node.setHeight(max(node.getLeft().getHeight(),node.getRight().getHeight()) + 1)
            if prev != node.getHeight():
                counter += 1
            balance_factor = node.getBalanceFactor()

            if balance_factor == -2:
                counter += AVLTreeList.rotate(tree_list, node, -2, node.getRight(), node.getRight().getBalanceFactor())

            if balance_factor == 2:
                counter += AVLTreeList.rotate(tree_list, node, 2, node.getLeft(), node.getLeft().getBalanceFactor())

            node = node.getParent()
        return counter

    @staticmethod
    def fixHeight(node):
        cnt = 0;
        currentNode = node;
        node.setHeight(max(node.getLeft().getHeight(), node.getRight().getHeight()) + 1)
        while (currentNode.getParent().isRealNode()):
            currentNode = currentNode.getParent()
            prevheight = currentNode.getHeight
            currentNode.setHeight(max(currentNode.getLeft().getHeight(), currentNode.getRight().getHeight()) + 1)
            if (prevheight == currentNode.getHeight()):
                return cnt
            cnt += 1
        return cnt

        




    """Perform rotations to balance an AVL tree

						@type tree_list: AVLTreeList
						@param tree_list: a pointer to the tree list
						@type node: AVLNode
						@param node: the node to start rotating from
						@type bf: int
						@param bf: balance factor of the given node
						@type child: AVLNode
						@param child: relevant child node
						@type child_bf: int
						@param child_bf: relevant child's balance factor
						@rtype: int
						@returns: number of rotations done
							"""

    @staticmethod
    def rotate(tree_list, node, bf, child, child_bf):
        # TODO: For simple rotations fix heights for node & child
        if bf == 2 and child_bf in [1, 0]:  # Right rotation
            node.setLeft(child.getRight())
            node.getLeft().setParent(node)
            child.setRight(node)
            child.setParent(node.getParent())
            child.getParent().setProperChild(tree_list, child, node)
            node.setParent(child)
            node.setSize(node.getRight().getSize() + node.getLeft().getSize() + 2)
            child.setSize(child.getRight().getSize() + child.getLeft().getSize() + 2)
            node.setHeight(max(node.getLeft().getHeight(), node.getRight().getHeight()) + 1)
            #AVLTreeList.fixHeight(node)
            return 1

        if bf == -2 and child_bf in [-1, 0]:  # Left rotation
            node.setRight(child.getLeft())
            node.getRight().setParent(node)
            child.setLeft(node)
            child.setParent(node.getParent())
            child.getParent().setProperChild(tree_list, child, node)
            node.setParent(child)
            node.setSize(node.getRight().getSize() + node.getLeft().getSize() + 2)
            child.setSize(child.getRight().getSize() + child.getLeft().getSize() + 2)
            node.setHeight(max(node.getLeft().getHeight(), node.getRight().getHeight()) + 1)
            #AVLTreeList.fixHeight(node)
            return 1

        if bf == 2 and child_bf == -1:  # Left then right rotation
            node.setLeft(child.getRight().getRight())
            child.getRight().getRight().setParent(node)
            child.getRight().setRight(node)
            child.getRight().getLeft().setParent(child)
            child.getRight().setParent(node.getParent())
            node.getParent().setProperChild(tree_list, child.getRight(), node)
            node.setParent(child.getRight())
            child.setRight(node.getParent().getLeft())
            child.setParent(node.getParent())
            node.getParent().setLeft(child)
            node.setSize(node.getRight().getSize() + node.getLeft().getSize() + 2)
            child.setSize(child.getRight().getSize() + child.getLeft().getSize() + 2)
            node.getParent().setSize(node.getParent().getRight().getSize() + node.getParent().getLeft().getSize() + 2)
            child.setHeight(max(child.getLeft().getHeight(), child.getRight().getHeight()) + 1)
            node.setHeight(max(node.getLeft().getHeight(), node.getRight().getHeight()) + 1)
            node.getParent().setHeight(max(node.getParent().getLeft().getHeight(), node.getParent().getRight().getHeight()) + 1)
            #AVLTreeList.fixHeight(node.getParent())
            return 2

        if bf == -2 and child_bf == 1:  # Right then left rotation
            node.setRight(child.getLeft().getLeft())
            child.getLeft().getLeft().setParent(node)
            child.getLeft().setLeft(node)
            child.getLeft().getRight().setParent(child)
            child.getLeft().setParent(node.getParent())
            node.getParent().setProperChild(tree_list, child.getLeft(), node)
            node.setParent(child.getLeft())
            child.setLeft(node.getParent().getRight())
            child.setParent(node.getParent())
            node.getParent().setRight(child)
            node.setSize(node.getRight().getSize() + node.getLeft().getSize() + 2)
            child.setSize(child.getRight().getSize() + child.getLeft().getSize() + 2)
            node.getParent().setSize(node.getParent().getRight().getSize() + node.getParent().getLeft().getSize() + 2)
            child.setHeight(max(child.getLeft().getHeight(), child.getRight().getHeight()) + 1)
            node.setHeight(max(node.getLeft().getHeight(), node.getRight().getHeight()) + 1)
            node.getParent().setHeight(max(node.getParent().getLeft().getHeight(), node.getParent().getRight().getHeight()) + 1)
            #AVLTreeList.fixHeight(node.getParent())
            return 2
    
    
    
