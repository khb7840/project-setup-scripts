# python3 code
# Generate script according to pre-defined template
# Author: Hyunbin Kim
# Date: 2020. 03. 20

# import necessary libraries
import os
import sys
import datetime
import collections
from generator.dir_generator import make_basedir

# TODO: The main class should be updated

# Program_language info
# assignment grammar uses f-string,
# python version should be 3.6 or higher
# Current version supports:
#   GO, JAVASCRIPT, TYPESCRIPT, PYTHON, R


class ScriptGenerator:
    # check variables & initialization
    def __init__(self):
        # get timetag
        self.now = datetime.datetime.now()
        self.timetag = self.now.strftime("%Y. %m. %d. %H:%M:%S")

        # set default values
        self.file_type = "python"
        self.file_extension = ".py"
        self.path = "".join([
            "./", self.now.strftime("%Y%m%d_%H%M%S"), self.file_extension
        ])

        # set empty variable names
        self.functions = ["example_function"]
        self.classes = ["ExampleClass"]
        self.variables = ["ex_var"]
        self.libraries = ["os"]
        self.contents = ""

        # set default author info
        self.author = "Hyunbin Kim"
        self.email = "khb7840@gmail.com"
        self.author_info = self.author + "(" + self.email + ")"
        self.description = ""

        # languages supported - current version
        self.__auto_script_availble = [
            "go", "typescript", "javascript", "python", "r"
        ]
        # program languages
        self.__program_lang_info = {
            "c": {"comment": "//", "extension": ".c"},
            "java": {"comment": "//", "extension": ".java"},
            "javascript": {
                "prefix": "// A javascript code",
                "comment": "//", "extension": ".js",
                "libraries": "\n".join(
                    [f'import * from "{lib}"' for lib in self.libraries]
                ),
                "function": "\n".join(
                    [f'''function {func}() {{\n    console.log("Hello, world!")\n}}''' for func in self.functions]
                ),
                "class": "\n".join(
                    [f'''class {cl} {{\n    name: string\n}}''' for cl in self.classes]
                ),
                "variable": "\n".join(
                    [f"let {self.variables} = null"]
                )
            },
            "go": {
                "prefix": "package main",
                "comment": "//", "extension": ".go",
                "libraries": "\n".join(
                    ["import ("] + ["\t" + lib for lib in self.libraries] + [")"]
                ),
                "function": "\n".join(
                    [f'''func {func}() {{\n    log.Println("{self.timetag}\n")}}''' for func in self.functions]
                ),
                "class": "\n".join(
                    [f'''type {cl} struct {{\n    // strVar string\n    // intVar int}}''' for cl in self.classes]
                ),
                "variable": "\n".join(
                    [f"{v} := nil" for v in self.variables]
                )
            },
            "typescript": {
                "prefix": "// A typescript code",
                "comment": "//", "extension": ".ts",
                "libraries": "\n".join(
                    [f'import * from "{lib}"' for lib in self.libraries]
                ),
                "function": "\n".join(
                    [f'''function {func}() {{\n    console.log("Hello, world!")\n}}''' for func in self.functions]),
                "class": "\n".join(
                    [f'''class {cl} {{\n    name: string\n}}''' for cl in self.classes]),
                "variable": "\n".join(
                    [f"let {v} = null" for v in self.variables]
                )
            },
            "dart": {"comment": "//", "extension": ".dart"},
            "python": {
                "prefix": "# python3 code",
                "comment": "#", "extension": ".py",
                "libraries": "\n".join(
                    [f"import {lib}" for lib in self.libraries]
                ),
                "function": "\n".join(
                    [f'''def {func}():\n    pass''' for func in self.functions]
                ),
                "class": "\n".join(
                    [f'''class {cl}:\n    __init__(self):\n        pass''' for cl in self.classes]
                ),
                "variable": "\n".join(
                    [f"{v} = None" for v in self.variables]
                )
            },
            "r": {
                "prefix": "# R code",
                "comment": "#", "extension": ".r",
                "libraries": "\n".join(
                    [f"library({lib})" for lib in self.libraries]
                ),
                "function": "\n".join(
                    [f'''{func} <- function() {{\n    return()\n}}''' for func in self.functions]
                ),
                "class": "\n".join(
                    [f'''{cl} <- list()''' for cl in self.classes]
                ),
                "variable": "\n".join(
                    [f'''{v} <- 0''' for v in self.variables]
                )
            },
            "perl": {"comment": "#", "extension": ".pl"},
            "ruby": {"comment": "#", "extension": ".rb"},
            "julia": {"comment": "#", "extension": ".jl"},
            "bash": {"comment": "#", "extension": ".sh"},
            "lua": {"comment": "--", "extension": ".lua"},
            "sql": {"comment": "--", "extension": ".sql"},
            "matlab": {"comment": "%", "extension": ".m"}
        }

    def set_type(self, file_type, verbose=True):
        self.file_type = file_type
        if file_type in self.__program_lang_info.keys():
            self.file_extension = self.__program_lang_info[file_type]["extension"]
        else:
            raise TypeError("Unknown file type: " + file_type)

        self.path = "".join([
            "./", self.now.strftime("%Y%m%d_%H%M%S"), self.file_extension
        ])
        if verbose == True:
            print("Modified filetype to " + self.file_type)

    # read config dictionary & set values
    def from_config(self, config_dict, verbose=True):
        # check if config_dict["type"] ==  "markdown"
        if config_dict["type"] not in self.__program_lang_info.keys():
            raise TypeError("Type should be predefined")
        # set values
        if "description" in config_dict.keys():
            self.description = config_dict["description"]
        # update libraires
        if "libraries" in config_dict.keys():
            self.libraries = config_dict["libraries"]

        function_list = []
        class_list = []
        variable_list = []

        if "define" in config_dict.keys():
            def_list = config_dict["define"]
            for entry in def_list:
                vtype, vname = entry.split(sep=":")
                if vtype == "function":
                    function_list.append(vname)
                elif vtype == "class":
                    class_list.append(vname)
                elif vtype == "variable":
                    variable_list.append(vname)

        self.set_type(config_dict["type"])
        self.path = config_dict["path"]
        self.functions = function_list
        self.classes = class_list
        self.variables = variable_list

        updated = update_script_info(
            type=self.file_type, liblist=self.libraries,
            funclist=self.functions, classlist=self.classes,
            varlist=self.variables
        )

        self.__program_lang_info[self.file_type].update(updated)

        if verbose == True:
            print("Config file loaded: " + config_dict["path"])

    def generate_contents(self, process="append"):
        # string to be returned
        generated_contents = ""
        # check if template for autoscripting is predefined
        # if not, return empty contents
        if self.file_type not in self.__auto_script_availble:
            return generated_contents

        # pre-defined script order
        #   1. prefix
        #   2. comment
        #       2.1 Author info
        #       2.2 Timetag
        #   3. library
        #   4. variable
        #   5. class
        #   6. function

        # empty list to save contents line by line
        contents_lines = []
        template = self.__program_lang_info[self.file_type]

        # prefix
        contents_lines.append(template["prefix"])
        # comment
        contents_lines.append(
            template["comment"] + " Author: " + self.author_info
        )
        if self.description != "":
            contents_lines.append(
                template["comment"] + " Description: " + self.description
            )
        contents_lines.append(
            template["comment"] + " Date: " + self.timetag
        )
        contents_lines.append("")
        # libraries
        contents_lines.append(template["libraries"])
        contents_lines.append("")
        # variable
        contents_lines.append(template["variable"])
        contents_lines.append("")
        # class
        contents_lines.append(template["class"])
        contents_lines.append("")
        # function
        contents_lines.append(template["function"])

        # set self.contents
        generated_contents = "\n".join(contents_lines)

        # type of process should be one of
        #   append / set / pass
        if process == "append":
            self.contents = generated_contents + self.contents
        elif process == "set":
            self.contents = generated_contents
        elif process == "pass":
            self.contents = self.contents
        else:
            raise ValueError("Unknown process name: " + process)

        # return
        return generated_contents

    def write(self, process="append", save=True, verbose=True):
        script_contents = self.generate_contents(process=process)
        make_basedir(self.path)
        script_file = open(self.path, "w")
        script_file.write(self.contents)
        script_file.close()
        if verbose == True:
            print("Successfully generated: " + self.path)
        pass


def update_script_info(type, liblist, funclist, classlist, varlist):
    if type == "python":
        output = {
            "libraries": "\n".join(
                [f"import {lib}" for lib in liblist]
            ),
            "function": "\n".join(
                [f'''def {func}():\n    pass''' for func in funclist]
            ),
            "class": "\n".join(
                [f'''class {cl}:\n    def __init__(self):\n        pass''' for cl in classlist]
            ),
            "variable": "\n".join(
                [f"{v} = None" for v in varlist]
            )
        }
    elif type == "r":
        output = {
            "libraries": "\n".join(
                [f"library({lib})" for lib in liblist]
            ),
            "function": "\n".join(
                [f'''{func} <- function() {{\n    return()\n}}''' for func in funclist]
            ),
            "class": "\n".join(
                [f'''{cl} <- list()''' for cl in classlist]
            ),
            "variable": "\n".join(
                [f'''{v} <- 0''' for v in varlist]
            )
        }
    elif type == "go":
        output = {
            "libraries": "\n".join(
                ["import ("] + [f'''\t"{lib}"''' for lib in liblist] + [")"]
            ),
            "function": "\n".join(
                [f'''func {func}() {{\n\tlog.Println("Hello, World!")\n}}''' for func in funclist]
            ),
            "class": "\n".join(
                [f'''type {cl} struct {{\n\t// strVar string\n\t// intVar int\n}}''' for cl in classlist]
            ),
            "variable": "\n".join(
                [f"{v} := nil" for v in varlist]
            )
        }

    elif type == "typescript":
        output = {
            "libraries": "\n".join(
                [f'import * from "{lib}"' for lib in liblist]
            ),
            "function": "\n".join(
                [f'''function {func}() {{\n    console.log("Hello, world!")\n}}''' for func in funclist]),
            "class": "\n".join(
                [f'''class {cl} {{\n    name: string\n}}''' for cl in classlist]),
            "variable": "\n".join(
                [f"let {v} = null" for v in varlist]
            )
        }
    elif type == "javascript":
        output = {
            "libraries": "\n".join(
                [f'import * from "{lib}"' for lib in liblist]
            ),
            "function": "\n".join(
                [f'''function {func}() {{\n    console.log("Hello, world!")\n}}''' for func in funclist]
            ),
            "class": "\n".join(
                [f'''class {cl} {{\n    name: string\n}}''' for cl in classlist]
            ),
            "variable": "\n".join(
                [f"let {v} = null" for v in varlist]
            )
        }

    return output
