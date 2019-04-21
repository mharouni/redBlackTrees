from Model.RbTree import Tree


tree = Tree()

tree.insert(8)
tree.insert(6)
tree.insert(4)
#print(tree.root)
tree.test(tree.root)
print(tree)
tree.leftLeft(tree.root.left.left,tree.root.left,tree.root)
tree.test(tree.root)

print(tree)



