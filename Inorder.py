

'''
InOrder Traversal 

Traverse in 
left 
root 
right 

'''


def InOrder(node):
    if node is None:
        return 
    InOrder(node.left)
    print(node.data , end = ' ')
    InOrder(node.right) 

    