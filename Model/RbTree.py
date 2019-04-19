from Model.Node import Node

class Tree:


    def __init__(self):
        self.root = None
        count = 0

    def insert(self,val):
        if not self.root:
            self.root= Node(val, None, True)
            self.count = 1
        else:
            parent = self._findParent(self.root, val)
            if parent:
                newNode = Node(val, parent, False)
                if parent.val < newNode.val:
                    parent.right = newNode
                else:
                    parent.left = newNode
                self.count += 1
              #  self._rebalance(newNode)#to be implemented
            else:
                raise Exception("Word {0} already in Dict".format(val))

    def _findParent(self,node,val)->Node:

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

    def search(self,val)-> Node:
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



    def _rebalance(self,node):



    def test(self,node):
        if node.left:
            self.test(node.left)
        if node.right:
            self.test(node.right)
        print(node)


