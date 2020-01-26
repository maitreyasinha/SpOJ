operators = ["+", "-", "*", "/"]
brackets = ["(",")"]
expression = "(a+b+c)"#"(a+(b*c))"

gen = (i for i in expression)

# class Node(object):
#     def __init__(self, node, val):
#         self.node = None
#         self.val = None

class Tree(object):
    def __init__(self):
        self.right = None
        self.left = None
        self.val = None

length = range(len(expression))

expr = expression

def create_tree2(expr):
    for i in expr:
        if i == "(":
            tree = Tree()
            mode = "left"
        elif i == ")":
            mode = "left"
        elif i in operators:
            tree.operator = i
            mode = "right"
        else:
            setattr(tree,mode,i)
    return tree

def create_tree3(expr):
    ctree = ntree
    for i in expr:
        if i == "(":
            pass
        elif i == ")":
            pass
        elif i in operators:
            pass
        else:
            ntree = Tree()
            ntree.val = i
            ntree.left = ctree
            ctree.right = ntree

    return tree

class TreeNext(object):
    def __init__(self, val, left, right):
        self.val = val
        self.right = right
        self.left = left

    def __str__(self):
        return self.val

l = []

def create_tree4():
    tree = None
    iteration = True
    while iteration == True:
        try:
            ch = next(gen)
            if ch in operators:
                pVal = l.pop(0)
                nVal = next(gen)
                tree = TreeNext(ch,nVal,pVal)
            else:
                l.insert(0,ch)
        except StopIteration:
            iteration = False
    return tree

def create_tree5():
    tree = None
    iteration = True
    ch = next(gen)
    stree = tree = TreeNext(ch, None,None)
    while iteration == True:
        try:

            if ch == "(":
                tree = create_tree5()
                pass
            elif ch == ")":
                return tree

            tree.right = TreeNext(ch, tree, None)
            tree = tree.right
        except StopIteration:
            iteration = False

    return stree

stree = create_tree5()
stree