class Node():
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

    def preList(self,root,prelist):
        if root == None:
            return
        prelist.append(root.data)
        self.preList(root.left,prelist)
        self.preList(root.right,prelist)
        return prelist
    def midList(self,root,midlist):
        if root == None:
            return
        self.midList(root.left,midlist)
        midlist.append(root.data)
        self.midList(root.right,midlist)
        return midlist
    def behindList(self,root,behindlist):
        if root == None:
            return
        self.behindList(root.left,behindlist)
        self.behindList(root.right,behindlist)
        behindlist.append(root.data)
        return behindlist

def preTraverse(root):
    '''
    前序遍历
    '''
    if root == None:
        return
    print(root.data)
    preTraverse(root.left)
    preTraverse(root.right)

def midTraverse(root):
    '''
    中序遍历
    '''
    if root == None:
        return
    midTraverse(root.left)
    print(root.data)
    midTraverse(root.right)

def afterTraverse(root):
    '''
    后序遍历
    '''
    if root == None:
        return
    afterTraverse(root.left)
    afterTraverse(root.right)
    print(root.data)

def rebuildPreTree(list=[]):
    print(list)
    if len(list) <= 0 :
        return
    mid = (len(list)-1)//2
    num = list.pop(0)
    root = Node(num)
    root.left = rebuildPreTree(list)
    root.right = rebuildPreTree(list)
    return root

if __name__ == "__main__":
    #tree = Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))
    prelist,midlist,behindlist,list_ = [],[],[],[]
    tree = Node(1,Node(2,Node(3),Node(4)),Node(5,Node(6),Node(7)))

    print("前中后遍历：")
    print(tree.preList(tree,prelist))
    print(tree.midList(tree,midlist))
    print(tree.behindList(tree,behindlist))

    print(("重建二叉树："))
    prel=[]
    prel = tree.preList(tree,prel)
    print("pre:")
    print(prel)
    new_tree = rebuildPreTree(prel)
    new_prelist = []
    new_prelist = tree.preList(new_tree,new_prelist)
    print("rebuilt:")
    print(new_prelist)



