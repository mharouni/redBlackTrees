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
                ex = "Word "+str(val)+" already in Dict"
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
        elif node.val < val:
            if node.right:
                return self._findNode(node.right, val)

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
        self._rotateLeft(node, parent, grandParent)
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


    def _getInorderSuccessor(self, node: Node)-> Node:
        if node.right is not None:
            return self._min(node.right)
        else:
            parent = node.parent
            while parent:
                if node is parent.right:
                    break
                else:
                    node = parent
                    parent = parent.parent
            return parent

    def _min(self, node: Node)-> Node:
        if node.left:
            return self._min(node.left)
        else:
            return node

    def remove(self, node: Node, value):
        if  node and value < node.val:
            return self.remove(node.left, value)
        elif node and value > node.val:
            return self.remove(node. right, value)
        elif node and value == node.val:
            nodeToRemove = node
            if node.right and node.left:
                suc = self._getInorderSuccessor(node)
                node.val = suc.val
                nodeToRemove = suc
               # print(nodeToRemove)
                #print(self.root)
            self._remove(nodeToRemove)
            self.count -= 1
        else:
            return




    def _remove(self, node: Node):
        leftChild = node.left
       # print(node)
        rightChild = node.right
        child = leftChild if node.left else rightChild
        if node is self.root:
            print("root")
            if child: #removing root while it has a single child
                self.root = child
                self.root.parent = None
                self.root.color = True
            else:
                self.root = None
        elif not node.color:
            if not (leftChild or rightChild):
                self._removeLeaf(node)
            else:
                raise Exception("BlackHeightError")
        else:#Node is black
            if leftChild:
                if leftChild.left or leftChild.right:
                    raise Exception("BlackNode red child problem1")
            if rightChild:
                if rightChild.right or rightChild.left:
                    raise Exception("BlackNode red child problem2")
            if child and (not child.color):#red child
                node.val = child.val
                node.left = child.left
                node.right = child.right
            else:#black child
                self._removeBlackNode(node)



    def _removeLeaf(self, node: Node):
        if node.val >= node.parent.val:
            node.parent.right = None
        else:
            node.parent.left = None

    def _removeBlackNode(self, node: Node):
        self._case1(node)
        self._removeLeaf(node)


    def _case1(self, node: Node):#removing root//terminating case
        if node is self.root:
            node.color = True
            return
        self._case2(node=node)

    def _case2(self, node: Node):#parent black sibiling red sibiling's children black or nill
        parent = node.parent
        if node is parent.left:
            sibiling = parent.right
        else:
            sibiling = parent.left
        if (not sibiling.color) and (parent.color) and ((not sibiling.left) or sibiling.left.color) and ((not sibiling.right) or sibiling.right.color):
            if sibiling is parent.left:
                self._rotateRight(node=None, parent=sibiling, grandParent=parent)
            else:
                self._rotateLeft(node=None, parent=sibiling, grandParent=parent)

            parent.color = False
            sibiling.color = True
            return self._case1(node=node)
        return self._case3(node=node)

    def _case3(self, node: Node):#all black
        parent = node.parent
        if node is parent.left:
            sibiling = parent.right
        else:
            sibiling = parent.left

        if parent.color and sibiling.color and ((not sibiling.left) or sibiling.left.color) and ((not sibiling.right) or sibiling.right.color):#potential runtime error
            sibiling.color = False
            return self._case1(node=parent)
        return self._case4(node=node)

    def _case4(self,node: Node):#parent red sibling black with black children
        parent = node.parent
        if not parent.color:
            if node is parent.left:
                sibling = parent.right
            else:
                sibling = parent.left
            if sibling.color and ((not sibling.left) or sibling.left.color) and ((not sibling.right) or sibling.right.color):#potential run time error
                parent.color = True
                sibling.color = False
            return
        return self._case5(node=node)

    def _case5(self,node: Node):
        parent = node.parent
        if node is parent.left:
            sibiling = parent.right
            closerNode = sibiling.left
            outerNode = sibiling.right
        else:
            sibiling = parent.left
            closerNode = sibiling.right
            outerNode = sibiling.left
        if (closerNode and (not closerNode.color)) and ((not outerNode) or outerNode.color) and sibiling.color:#potential runtime error
            if sibiling and (sibiling is parent.left):
                self._rotateLeft(node=None, parent=closerNode, grandParent=sibiling)
            else:
                self._rotateLeft(node=None, parent=closerNode, grandParent=sibiling)
            closerNode.color = True
            sibiling.color = False

        self._case6(node=node)

    def _case6(self,node: Node):
        parent = node.parent
        if node is parent.left:
            sibling = parent.right
            outerNode = sibling.right
        else:
            sibling = parent.left
            outerNode = sibling.left
        if sibling.color and sibling.color and outerNode and (not outerNode.color):
            parentColor = parent.color
            if sibling is parent.left:
                self._rotateRight(node=None, parent=sibling, grandParent=parent)
            else:
                self._rotateLeft(node=None, parent=sibling, grandParent=parent)
            sibling.color = parentColor
            sibling.right.color = True
            sibling.left.color = True
            return
        raise Exception("Removal should've been Done")

    def test(self,node):
        if node.left:
            self.test(node.left)
        print(node)
        if node.right:
            self.test(node.right)





