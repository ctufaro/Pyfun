class Tree(object):
	def __init__(self):
		self.left = None
		self.right = None
		self.data = None
		
root = Tree()
root.data = "1"
root.left = Tree()
root.left.data = "2"
root.right = Tree()
root.right.data = "3"
 
root.left.left = Tree()
root.left.left.data = "4"
root.left.right = Tree()
root.left.right.data = "5"

def inorder_ite(root):
    #visit left, print root, visit right
    stack = []
    while True:
        if root!=None:
            stack.append(root)
            root = root.left
        else:
            if(len(stack) > 0):
                root = stack.pop()
                print(root.data)
                root = root.right
            else:
                break            

def preorder_ite(root):
    #print root, visit left, visit right
    stack = []
    stack.append(root)
    while True:
        if(len(stack) > 0):
            root = stack.pop()
            print(root.data)
            if root.right!=None:
                stack.append(root.right)
            if root.left!=None:
                stack.append(root.left)

        else:
            break

inorder_ite(root)
print('\n')
preorder_ite(root)
