'''

PreOrder Traversal 
Iterate the Root , Left , Right 
Print the root data  
Recursively call the left and right 


'''

def PreOrder(node):
    if node is None:
        return 
    print(node.data, end = ' ')
    PreOrder(node.left)
    PreOrder(node.right)

    
    