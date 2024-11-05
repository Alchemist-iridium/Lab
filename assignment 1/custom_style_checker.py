import ast
import re
import os

class StyleChecker:
    def __init__(self, filename):
        self.filename = filename
        self.tree = None
        self.content = ""
        self.imports = []
        self.classes = []
        self.functions = []
        self.type_annotation_issues = []
        self.naming_convention_issues = []

    def read_file(self):
        print(f"Reading file: {self.filename}")
        try:
            with open(self.filename, 'r') as file:
                self.content = file.read()
                self.tree = ast.parse(self.content)
            print("File read successfully.")
        except FileNotFoundError:
            print(f"Error: File {self.filename} not found.")
            raise
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            raise

    def analyze_imports(self):
        print("Analyzing imports...")
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    self.imports.append(alias.name)
            elif isinstance(node, ast.ImportFrom):
                module = node.module
                for alias in node.names:
                    self.imports.append(f"{module}.{alias.name}")
        print("Imports analyzed.")

    def analyze_classes_and_functions(self):
        print("Analyzing classes and functions...")
        for node in ast.walk(self.tree):
            if isinstance(node, ast.ClassDef):
                self.classes.append(node)
            elif isinstance(node, ast.FunctionDef):
                if not any(isinstance(parent, ast.ClassDef) for parent in ast.walk(self.tree) if isinstance(parent, ast.ClassDef) and node in parent.body):
                    self.functions.append(node)
        print("Classes and functions analyzed.")

    def extract_docstrings(self):
        print("Extracting docstrings...")
        docstring_info = []
        for cls in self.classes:
            docstring = ast.get_docstring(cls)
            if docstring:
                docstring_info.append(f"Class {cls.name}: {docstring}\n")
            else:
                docstring_info.append(f"Class {cls.name}: DocString not found.\n")
            for item in cls.body:
                if isinstance(item, ast.FunctionDef):
                    method_docstring = ast.get_docstring(item)
                    if method_docstring:
                        docstring_info.append(f"Method {cls.name}.{item.name}: {method_docstring}\n")
                    else:
                        docstring_info.append(f"Method {cls.name}.{item.name}: DocString not found.\n")

        for func in self.functions:
            docstring = ast.get_docstring(func)
            if docstring:
                docstring_info.append(f"Function {func.name}: {docstring}\n")
            else:
                docstring_info.append(f"Function {func.name}: DocString not found.\n")
        print("Docstrings extracted.")
        return docstring_info

    def analyze_type_annotations(self):
        print("Analyzing type annotations...")
        for func in self.functions:
            if not all(arg.annotation for arg in func.args.args) or not func.returns:
                self.type_annotation_issues.append(func.name)
        for cls in self.classes:
            for item in cls.body:
                if isinstance(item, ast.FunctionDef):
                    if not all(arg.annotation for arg in item.args.args) or not item.returns:
                        self.type_annotation_issues.append(f"{cls.name}.{item.name}")
        print("Type annotations analyzed.")

    def analyze_naming_conventions(self):
        print("Analyzing naming conventions...")
        class_name_pattern = re.compile(r'^[A-Z][a-zA-Z0-9]+$')
        function_name_pattern = re.compile(r'^[a-z_][a-z0-9_]*$')

        for cls in self.classes:
            if not class_name_pattern.match(cls.name):
                self.naming_convention_issues.append(f"Class {cls.name} does not follow CamelCase naming convention.")

        for func in self.functions:
            if not function_name_pattern.match(func.name):
                self.naming_convention_issues.append(f"Function {func.name} does not follow snake_case naming convention.")
        for cls in self.classes:
            for item in cls.body:
                if isinstance(item, ast.FunctionDef) and not function_name_pattern.match(item.name):
                    self.naming_convention_issues.append(f"Method {cls.name}.{item.name} does not follow snake_case naming convention.")
        print("Naming conventions analyzed.")

    def generate_report(self):
        report_filename = f"style_report_{os.path.splitext(os.path.basename(self.filename))[0]}.txt"
        print(f"Generating report: {report_filename}")
        try:
            with open(report_filename, 'w') as report:
                report.write(f"File: {self.filename}\n")
                report.write(f"Total Lines: {len(self.content.splitlines())}\n\n")

                report.write("Imports:\n")
                if self.imports:
                    for imp in self.imports:
                        report.write(f"  {imp}\n")
                else:
                    report.write("  None\n")
                report.write("\n")

                report.write("Classes:\n")
                if self.classes:
                    for cls in self.classes:
                        report.write(f"  {cls.name}\n")
                else:
                    report.write("  None\n")
                report.write("\n")

                report.write("Functions:\n")
                if self.functions:
                    for func in self.functions:
                        report.write(f"  {func.name}\n")
                else:
                    report.write("  None\n")
                report.write("\n")

                report.write("DocStrings:\n")
                docstrings = self.extract_docstrings()
                for docstring in docstrings:
                    report.write(f"  {docstring}\n")
                report.write("\n")

                report.write("Type Annotation Issues:\n")
                if self.type_annotation_issues:
                    for issue in self.type_annotation_issues:
                        report.write(f"  {issue}\n")
                else:
                    report.write("  All functions and methods use type annotations.\n")
                report.write("\n")

                report.write("Naming Convention Issues:\n")
                if self.naming_convention_issues:
                    for issue in self.naming_convention_issues:
                        report.write(f"  {issue}\n")
                else:
                    report.write("  All names adhere to the naming convention.\n")
            print(f"Report generated successfully: {report_filename}")
        except Exception as e:
            print(f"An error occurred while generating the report: {e}")

    def run(self):
        print("Starting style check...")
        self.read_file()
        self.analyze_imports()
        self.analyze_classes_and_functions()
        self.analyze_type_annotations()
        self.analyze_naming_conventions()
        self.generate_report()
        print("Style check completed.")

if __name__ == "__main__":
    filename = "custom_style_checker.py"  # Replace with the actual file you want to analyze
    checker = StyleChecker(filename)
    checker.run()
