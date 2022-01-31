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

    def maximum_value(self,root):
            if (root == None):
                return 0
            start_value=root.value
            left_max=self.maximum_value(root.left)
            right_max=self.maximum_value(root.right)
            if (left_max>start_value):
                start_value=left_max
            if(right_max>start_value):
                start_value=right_max

            return start_value

