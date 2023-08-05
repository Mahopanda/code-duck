import ast

class FunctionAndClassVisitor(ast.NodeVisitor):
    def __init__(self):
        self.functions = []
        self.classes = []

    def visit_FunctionDef(self, node):
        source_code = ast.unparse(node)
        self.functions.append(source_code)
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        source_code = ast.unparse(node)
        self.classes.append(source_code)
        self.generic_visit(node)