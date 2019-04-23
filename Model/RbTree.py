from Model.Node import Node


class Tree:

    def __init__(self):
        self.root = None
        self.count = 0

    def __repr__(self):
        return "{0} Elements with height {1} ".format(self.count, self._getHeight())

    def insert(self, val: str):
        if not self.root:
            self.root = Node(val, None, True)
            self.count = 1
        else:
            parent = self._findParent(self.root, val)
            if parent:
                newNode = Node(val, parent, False)
                if parent < newNode:
                    parent.right = newNode
                elif parent > newNode:
                    parent.left = newNode
                self._fixInsert(newNode)  # to be implemented
                self.count += 1

            else:
                ex = "Word "+val+" already in Dict"
                raise Exception(ex)

    def _findParent(self, node, val)->Node:

        if node.val == val:
            return None
        else:
            if node.val > val:

                if (not node.left) and (not node.right):
                    return node
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
        if node.val == val:
            return node
        if (not node.left) and (not node.right):
            return None
        elif node.val > val:
            if node.left:
                return self._findNode(node.left, val)
          #  else:
           #     return None
        elif node.val < val:
            if node.right:
                return self._findNode(node.right, val)
            #else:
             #   return None


    def _getHeight(self)-> int:

            height = self._traverseHeight(self.root)
            return height

    def _traverseHeight(self, node: Node)->int:

        if not node:

            return 0
        else:
            leftHeight = self._traverseHeight(node.left)
            rightHeight = self._traverseHeight(node.right)
            if leftHeight > rightHeight:
                return leftHeight + 1
            else:
                return rightHeight + 1



    def _fixRotation(self, parent :Node, grandParent : Node, greatGrandParent : Node):
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
        self._fixRotation(parent, grandParent, greatGrandParent)
        oldLeft = parent.left
        parent.left = grandParent
        grandParent.parent = parent
        grandParent.right = oldLeft
        if oldLeft:
            oldLeft.parent = grandParent


    def _rotateRight(self, node : Node, parent : Node, grandParent: Node):
        greatGrandParent = grandParent.parent
        self._fixRotation(parent, grandParent, greatGrandParent)
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
        self._rotateLeft(node, parent , grandParent)
        parent.swapColor()
        grandParent.swapColor()


    def _rightLeft(self, node :Node, parent: Node, grandParent: Node):
        self._rotateRight(None, node, parent)
        self._rightRight(node, parent, grandParent)

    def _leftRight(self, node: Node, parent: Node,grandParent: Node):
        self._rotateLeft(None, node, parent)
        self._leftLeft(node, parent, grandParent)

    def _recolor(self, grandParent: Node):
        grandParent.left.color = True
        grandParent.right.color = True
        if grandParent is not self.root:
            grandParent.color = False
        else:
            grandParent.color = True
            self._fixInsert(grandParent)

    def _fixInsert(self, node: Node):
        parent = node.parent
        if (not parent) or (not parent.parent) or (node.color or parent.color):
            return
        else:
            grandParent = parent.parent
            if parent is grandParent.left:
                uncle = grandParent.right
            else:
                uncle = grandParent.left
        if uncle and (not uncle.color):#uncle is red
            self._recolor(grandParent)
        else:
            if parent is grandParent.left and (node is parent.left):
                self._leftLeft(node, parent, grandParent)
            elif parent is grandParent.right and (node is parent.right):
                self._rightRight(node, parent, grandParent)
            elif parent is grandParent.left and (node is parent.right):
                self._leftRight(node, parent, grandParent)
            elif parent is grandParent.right and (node is parent.left):

                self._rightLeft(node, parent, grandParent)




    def test(self,node):
        if node.left:
            self.test(node.left)
        print(node)
        if node.right:
            self.test(node.right)



