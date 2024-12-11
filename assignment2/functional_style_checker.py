import os
import re
import sys
import ast
from typing import List, Tuple

def get_python_file_path() -> str:
    """
    Prompt the user for a Python file path and sanitize input.
    """
    path = input("Enter the path to the Python source file: ").strip()
    return path.strip('\"\'')


def read_file_content(file_path: str) -> str:
    """
    Read the content of the given file.
    """
    with open(file_path, 'r') as file:
        return file.read()

def parse_python_file(file_content: str) -> ast.Module:
    """
    Parse the file content into an AST (Abstract Syntax Tree).
    """
    return ast.parse(file_content)

def get_total_lines(file_content: str) -> int:
    """
    Get the total number of lines in the file.
    """
    return len(file_content.splitlines())

def get_imports(tree: ast.Module) -> List[str]:
    """
    Get a list of imported packages.
    """
    return [
        node.names[0].name for node in tree.body
        if isinstance(node, ast.Import)
    ]

def get_classes(tree: ast.Module) -> List[ast.ClassDef]:
    """
    Get a list of class definitions.
    """
    return [node for node in tree.body if isinstance(node, ast.ClassDef)]

def get_functions(tree: ast.Module) -> List[ast.FunctionDef]:
    """
    Get a list of functions (excluding methods within classes).
    """
    return [node for node in tree.body if isinstance(node, ast.FunctionDef)]

def extract_docstring(node) -> str:
    """
    Extract the docstring from a node (class, method, or function).
    """
    return ast.get_docstring(node)

def get_functions_without_annotations(tree: ast.Module) -> List[str]:
    """
    Get a list of functions and methods without type annotations.
    """
    def has_type_annotations(func_node: ast.FunctionDef) -> bool:
        return bool(func_node.args.args) and any(arg.annotation for arg in func_node.args.args)
    
    functions = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if not has_type_annotations(node):
                functions.append(node.name)
    return functions

def check_naming_conventions(classes: List[ast.ClassDef], functions: List[ast.FunctionDef]) -> Tuple[List[str], List[str]]:
    """
    Check naming conventions for classes and functions.
    """
    class_pattern = re.compile(r'^[A-Z][a-zA-Z0-9]*$')
    function_pattern = re.compile(r'^[a-z_][a-z0-9_]*$')
    
    bad_class_names = [cls.name for cls in classes if not class_pattern.match(cls.name)]
    bad_function_names = [func.name for func in functions if not function_pattern.match(func.name)]
    
    return bad_class_names, bad_function_names

def generate_report(file_path: str) -> None:
    """
    Generate a style report and save it to a file.
    """
    file_content = read_file_content(file_path)
    tree = parse_python_file(file_content)
    total_lines = get_total_lines(file_content)
    imports = get_imports(tree)
    classes = get_classes(tree)
    functions = get_functions(tree)
    
    class_docstrings = [
        (cls.name, extract_docstring(cls) or f"{cls.name}: DocString not found")
        for cls in classes
    ]
    
    function_docstrings = [
        (func.name, extract_docstring(func) or f"{func.name}: DocString not found")
        for func in functions
    ]
    
    functions_without_annotations = get_functions_without_annotations(tree)
    bad_class_names, bad_function_names = check_naming_conventions(classes, functions)
    
    report_lines = [
        f"File Structure: {os.path.basename(file_path)}",
        f"Total Number of Lines: {total_lines}\n",
        "Imports:",
        "\n".join(imports) if imports else "No imports found.",
        "\n",
        "Classes:",
        "\n".join([cls.name for cls in classes]) if classes else "No classes found.",
        "\n",
        "Functions:",
        "\n".join([func.name for func in functions]) if functions else "No functions found.",
        "\n",
        "DocStrings:",
    ]
    
    for name, docstring in class_docstrings:
        report_lines.append(f"Class {name}:\n{docstring}\n")
    
    for name, docstring in function_docstrings:
        report_lines.append(f"Function {name}:\n{docstring}\n")
    
    if functions_without_annotations:
        report_lines.append("\nFunctions/Methods without type annotations:")
        report_lines.extend(functions_without_annotations)
    else:
        report_lines.append("\nAll functions and methods use type annotations.")
    
    if bad_class_names or bad_function_names:
        report_lines.append("\nNaming Convention Issues:")
        if bad_class_names:
            report_lines.append("Classes with incorrect naming conventions:")
            report_lines.extend(bad_class_names)
        if bad_function_names:
            report_lines.append("Functions with incorrect naming conventions:")
            report_lines.extend(bad_function_names)
    else:
        report_lines.append("\nAll names adhere to the specified naming conventions.")
    
    output_file = f"style_report_{os.path.basename(file_path).replace('.py', '')}.txt"
    output_path = os.path.join(os.path.dirname(file_path), output_file)
    
    with open(output_path, 'w') as report:
        report.write("\n".join(report_lines))
    
    print(f"Report generated: {output_path}")

def main() -> None:
    """
    Main function to execute the script.
    """
    file_path = get_python_file_path()
    if not os.path.isfile(file_path) or not file_path.endswith(".py"):
        print("Invalid file path. Please provide a valid Python source file.")
        return
    generate_report(file_path)

if __name__ == "__main__":
    main()
