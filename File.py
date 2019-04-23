from Model.RbTree import Tree

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


    def search(self, word):
        self.tree.search(word)


    def insert(self, word):
        self.tree.insert(word)
        fileWriter = open("Dict.txt", "a")
        fileWriter.tell()
        fileWriter.seek(fileWriter.tell())
        fileWriter.write(str(word)+"\n")







f =File()
f.load()

f.tree.test(f.tree.root)
f.insert("Ahmed")
