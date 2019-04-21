from Model.Node import Node


class Tree:

    def __init__(self):
        self.root = None
        self.count = 0

    def __repr__(self):
        return "{0} Elements with height {1} ".format(self.count, self._getHeight())

    def insert(self,val):
        if not self.root:
            self.root= Node(val, None, True)
            self.count = 1
        else:
            parent = self._findParent(self.root, val)
            if parent:
                newNode = Node(val, parent, False)
                if parent < newNode:
                    parent.right = newNode
                elif parent > newNode:
                    parent.left = newNode
                self.count += 1
                #self._insertRebalance(newNode)#to be implemented
            else:
                raise Exception("Word {0} already in Dict".format(val))

    def _findParent(self, node, val)->Node:

        if (not node.left) and (not node.right):
            return node
        if node.val > val:

            if node.left:
                return self._findParent(node.left, val)
            else:
                return node
        elif node.val < val:

            if node.right:
                return self._findParent(node.right, val)
            else:
                return node
        elif node.val == val:
            return None

    def search(self, val)-> Node:
        if not self.root:
            print("Nothing inserted")
            return None
        else:
            targetNode = self._findNode(self.root, val)
            if targetNode:
                return targetNode
            else:
                print("Not Found")
                return None

    def _findNode(self, node, val):
        if not (node.left or node.right):
            return None
        elif node.val > val:
            if node.left:
                return self._findNode(node.left, val)
            else:
                return None
        elif node.val < val:
            if node.right:
                return self._findNode(node.right, val)
            else:
                return None
        elif node.val == val:
            return node

    def _getHeight(self)-> int:

        if self.root:
            height = 1
            height = self._traverseHeight(self.root, height)
            return height


        else:
            return 0

    def _traverseHeight(self,node: Node, height: int)->int:
        if node.left or node.right:
            height += 1
            if node.left:
                return self._traverseHeight(node.left, height)
            if node.right:
                return self._traverseHeight(node.right, height)
        else:
            return height

    def _update(self,parent :Node, grandParent : Node , greatGrandParent : Node):
        parent.parent = greatGrandParent
        if greatGrandParent:
            if greatGrandParent > grandParent:
                greatGrandParent.left = parent
            else:
                greatGrandParent.right = parent
        else:
            self.root = parent



    def _rotateLeft(self, node : Node, parent : Node, grandParent: Node):
        greatGrandParent = grandParent.parent
        self._update(parent, grandParent, greatGrandParent)
        oldLeft = parent.left
        parent.right = grandParent
        grandParent.parent = parent
        grandParent.right = oldLeft
        if oldLeft:
            oldLeft.parent = grandParent


    def _rotateRight(self, node : Node, parent : Node, grandParent: Node):
        greatGrandParent = grandParent.parent
        self._update(parent, grandParent, greatGrandParent)
        oldRight = parent.right
        parent.right = grandParent
        grandParent.parent = parent
        grandParent.left = oldRight
        if oldRight:
            oldRight.parent = grandParent

    def _leftLeft(self, node: Node,parent: Node, grandParent: Node):

        self._rotateRight(node, parent ,grandParent)
        parent.swapColor()
        grandParent.swapColor()

    def _rightRight(self,node: Node,parent: Node, grandParent: Node):
        self._rotateLeft(node, parent ,grandParent)
        parent.swapColor()
        grandParent.swapColor()


    def _rightLeft(self, node :Node, parent: Node, grandParent: Node):
        self._rotateRight(None, node, parent)
        self._rightRight(node, parent, grandParent)

    def _leftRight(self, node :Node, parent: Node, grandParent: Node):
        self._rotateLeft(None, Node, parent)
        self._leftLeft(node,parent,grandParent)

    def _recolor(self, x:Node):




 







    def test(self,node):
        if node.left:
            self.test(node.left)
        print(node)
        if node.right:
            self.test(node.right)



