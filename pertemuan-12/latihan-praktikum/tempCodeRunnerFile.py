def traverse_postorder(self, node, result):
        if node:
            self.traverse_postorder(node.left, result)
            self.traverse_postorder(node.right, result)
            result.append(node.data)
        return " - ".join(result)