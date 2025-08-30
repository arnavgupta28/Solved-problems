
'''
PostOrder 
left 
right 
print node 

'''
def PostOrder(node):
    if node is None:
        return 

    PostOrder(node.left)
    PostOrder(node.right)
    print(node.data)