class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

def print_tree(root, space=0, t=0):
    COUNT =3

    if root is None:
        return

    space+=COUNT
    # process right child
    print_tree(root.right,space, 1)

    for x in range(COUNT,space):
        print(" ",end="")
    if t==1: #right node    
        print(" / ",root.data)
    elif t==2: #left node
        print(" \ ",root.data)
    else: #root node
        print(root.data)

    #process left child
    print_tree(root.left,space,2)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)

print_tree(root)