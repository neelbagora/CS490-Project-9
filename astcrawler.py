import ast

def traverse_ast(file):
  for node in ast.walk(file):
    print(f'Nodetype: {type(node).__name__:{16}} {node}')
