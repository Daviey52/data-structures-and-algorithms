
from Trees.binary_tree import BinaryTree ,Node
def tree_intersection(b1 ,b2):
    b1 = BinaryTree()
    b2 = BinaryTree()

    values=[]
    data1= b1.pre_order()
    data2 = b2.pre_order()

    for i in data1:
        for j in data2:
            if i == j:
                values.append(i)
                j =+1
        i +=1

    return values

if __name__ == "__main__":
    Bt1 = BinaryTree()
    Bt1.root = Node(6)
    Bt1.root.right = Node(9)
    Bt1.root.left = Node(2)
    Bt1.root.left.left = Node(0)
    Bt1.root.right.left = Node(10)

    Bt2 = BinaryTree()
    Bt2.root = Node(6)
    Bt2.root.right = Node(2)
    Bt2.root.left = Node(10)
    Bt2.root.left.left = Node(18)
    print(tree_intersection(Bt1,Bt2))


