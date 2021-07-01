class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
    def insert(self,data):
        if(self.data):
            if(data < self.data):
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif  data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

    def printtree(self):
        if self.left:
            (".")
            self.left.printtree()
        print(self.data)
        if self.right:
            print("-")
            self.right.printtree()
            
def printTree(node, level=0):
        if node != None:
            printTree(node.left, level + 1)
            print(' ' * 4 * level + '->', node.data)
            printTree(node.right, level + 1)
            
def height(root):
    #if root is None return 0
        if root==None:
            return 0
        #find height of left subtree
        hleft=height(root.left)
        #find the height of right subtree
        hright=height(root.right)  
        #find max of hleft and hright, add 1 to it and return the value
        if hleft>hright:
            return hleft+1
        else:
            return hright+1
 

def CheckBalancedBinaryTree(root):
    if root==None:
        return True
    lheight= height(root.left)
    rheight = height(root.right)
    if(abs(lheight-rheight)>1):
        return False
    lcheck=CheckBalancedBinaryTree(root.left)
    rcheck=CheckBalancedBinaryTree(root.right)
    if lcheck==True and rcheck==True:
        return True
            
root = Node(1)
root.insert(2)
root.insert(3)
root.insert(4)
root.insert(5)
root.insert(6)
root.insert(7)
root.insert(8)
root.insert(9)
root.insert(10)
printTree(root)
print(height(root))
res = CheckBalancedBinaryTree(root)
print(res)
