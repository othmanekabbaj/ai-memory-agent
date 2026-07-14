import ast
import os


class CodeAnalyzer:

    def analyze(self, path: str):

        extension = os.path.splitext(path)[1]

        if extension == ".py":
            return self.analyze_python(path)

        if extension in [".js", ".jsx", ".ts", ".tsx"]:
            return self.analyze_javascript(path)

        return {}


    def analyze_python(self, path: str):

        result = {
            "classes": [],
            "functions": [],
            "imports": []
        }

        try:
            with open(
                path,
                "r",
                encoding="utf-8"
            ) as file:

                content = file.read()


            tree = ast.parse(content)


            for node in ast.walk(tree):

                if isinstance(node, ast.ClassDef):
                    result["classes"].append(
                        node.name
                    )

                elif isinstance(node, ast.FunctionDef):
                    result["functions"].append(
                        node.name
                    )

                elif isinstance(node, ast.Import):
                    for name in node.names:
                        result["imports"].append(
                            name.name
                        )

                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        result["imports"].append(
                            node.module
                        )


        except Exception:
            pass


        return result



    def analyze_javascript(self, path: str):

        result = {
            "components": [],
            "functions": [],
            "imports": []
        }

        try:
            with open(
                path,
                "r",
                encoding="utf-8"
            ) as file:

                content = file.read()


            lines = content.splitlines()


            for line in lines:

                line = line.strip()


                if line.startswith("import"):
                    result["imports"].append(
                        line
                    )


                if "function " in line:
                    name = line.split(
                        "function "
                    )[1].split("(")[0]

                    result["functions"].append(
                        name
                    )


                if "export default function" in line:

                    name = line.split(
                        "function "
                    )[1].split("(")[0]

                    result["components"].append(
                        name
                    )


        except Exception:
            pass


        return result