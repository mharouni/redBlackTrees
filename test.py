from Model.RbTree import Tree


tree = Tree()
for i in range(0,10):
    tree.insert(i)


tree.test(tree.root)
print( (tree.root >tree.root.right))