class Tree:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.data)
def printTree(Tree=Tree):
    if __name__ == '__main__':
        if Tree is None:
            return
        printTree(Tree.left)
        print(Tree.data)
        printTree(Tree.right)


def evaluate_expression(expr):
    root = Tree()
    for i in expr:
        if i == "(":
            root.left = Tree()
        if i in ["+","-","/","*"]:
            root.data = i
            root.right = Tree(i)
        if i.isdigit():
            root.left = i
    print(root.data)
#    printTree(root)


expression = "(2+2)"
evaluate_expression(expression)
