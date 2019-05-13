from Model.RbTree import Tree
from Model.Node import Node

class File:
    def __init__(self):
        self.tree = Tree()

    def load(self):

        try:

            fileReader = open("Dict.txt", "r")

        except IOError:
            print("Error")

        for line in fileReader:
            line = line.replace("\n", "")
            self.tree.insert(line)
        fileReader.close()
        print(self.tree)
        return

    def search(self, word):
        target = self.tree.search(word)
        if target:
            print("target: " + str(target) + " was Found")
        else:
            print ("target: " + str(target) + " was not Found")
        return

    def insert(self, word):
        self.tree.insert(word)
        fileWriter = open("Dict.txt", "a")
        fileWriter.seek(fileWriter.tell())
        fileWriter.write(str(word)+"\n")
        fileWriter.close()
        print(self.tree)
        return

    def remove(self, word):
        writer = open("Dict.txt", "w")
        self.tree.remove(self.tree.root, word)

        self._traverseTree(self.tree.root,writer)

        writer.close()
        print(self. tree)

    def _traverseTree(self,node:Node,writer):
        if node.left:
            self._traverseTree(node.left,writer)
        writer.seek(writer.tell())
        writer.write(str(node.val)+"\n")
        if node.right:
            self._traverseTree(node.right,writer)




