class Tree(object):
	def __init__(self):
		self.left = None
		self.right = None
		self.data = None
		
root = Tree()
root.data = "1"
root.left = Tree()
root.left.data = "3"
root.right = Tree()
root.right.data = "2" 
root.left.left = Tree()
root.left.left.data = "5"

root2 = Tree()
root2.data = "2"
root2.left = Tree()
root2.left.data = "1"
root2.right = Tree()
root2.right.data = "3"
root2.left.right = Tree()
root2.left.right.data = "4"
root2.right.right = Tree() 
root2.right.right.data = "7"

def preorder(root):
    if(root!=None):        
        print(root.data)
        preorder(root.left)
        preorder(root.right)

#output:3,4,5,4,5,7
def mergetrees(t1, t2):    
    if (t1 == None):
        return t2
    stack = []
    stack.append((t1, t2))
    while (len(stack)>0): 
        t = stack.pop()

        if (t[0] == None or t[1] == None):
            continue

        t[0].data = int(t[0].data) + int(t[1].data)

        if (t[0].left == None):
            t[0].left = t[1].left         
        else:
            stack.append((t[0].left, t[1].left))        

        if (t[0].right == None):
            t[0].right = t[1].right
        else:
            stack.append((t[0].right, t[1].right))        
      
    return t1

mt = mergetrees(root,root2)
preorder(mt)




