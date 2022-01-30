class BinaryTree:
    def __init__(self,root=None):
        self.root = root

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
    def in_order():
        ## left > root > right
        pass

    def post_order():
        # left > right > root
        pass



