class BinaryTree:
    def __init__(self,root=None):
        self.root = root
        self.left = None
        self.right = None

    def pre_order(self):
        ## root > left > right
        values = []
        def traverse(root):
            if root is None:
                return
            values.append(root.value)
            traverse(root.left)
            traverse(root.right)
        traverse(self.root)
        return values
    def in_order(self):
        ## left > root > right
        values = []
        def traverse(root):
            if root is None:
                return
            traverse(root.left)
            values.append(root.value)
            traverse(root.right)
        traverse(self.root)
        return values

    def post_order(self):
        # left > right > root
        values = []
        def traverse(root):
            if root is None:
                return
            traverse(root.left)
            traverse(root.right)
            values.append(root.value)
        traverse(self.root)
        return values



