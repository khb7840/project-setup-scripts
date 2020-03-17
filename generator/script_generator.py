# python3 code
# Modified from new_markdown_doc.py
# Author: Hyunbin Kim

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


class ScriptGenerator:
    # check variables & initialization
    def __init__(self, config_dict):
        # get timetag
        now = datetime.datetime.now()
        self.timetag = now.strftime("%Y. %m. %d. %H:%M:%S")

        # set default values
        self.file_type = "python"
        self.file_extension = ".py"
        self.path = "".join([
            "./", now.strftime("%YY%mm%dd_%HH%MM%SS"), self.file_extension
        ])

        # set empty variable names
        self.function_name = "example_function"
        self.class_name = "ExampleClass"
        self.variable_name = "ex_var"
        self.libraries = ["os"]

        # set default author info
        self.author = "Hyunbin Kim"
        self.email = "khb7840@gmail.com"
        self.author_info = self.author + "(" + self.email + ")"

        # program languages
        self.__program_lang_info = {
            "c": {"comment": "//", "extension": ".c"},
            "java": {"comment": "//", "extension": ".java"},
            "javascript": {"comment": "//", "extension": ".js"},
            "go": {
                "prefix": "package main",
                "comment": "//", "extension": ".go",
                "libraries": "\n".join(
                    ["import ("] + ["\t" + lib for lib in self.libraries] + [")"]
                ),
                "function":
                    f'''func {self.function_name}() {{
                        fmt.Println("{self.timetag}")
                    }}''',
                "struct":
                    f'''type {self.class_name} struct {{
                        // strVar string
                        // intVar int
                    }}''',
                "variable":
                    f'''{self.variable_name} := nil'''
            },
            "typescript": {
                "prefix": "// A typescript code",
                "comment": "//", "extension": ".ts"
            },
            "dart": {"comment": "//", "extension": ".dart"},
            "python": {
                "prefix": "# python3 code",
                "comment": "#", "extension": ".py",
                "libraries": [f"import {lib}" for lib in self.libraries],
                "function":
                    f'''def {self.function_name}():
                        pass''',
                "class":
                    f'''class {self.class_name}:
                        __init__(self):
                            pass''',
                "variable":
                    f"{self.variable_name} = None"
            },
            "r": {
                "prefix": "# R code",
                "comment": "#", "extension": ".r",
                "libraries": [f"library({lib})" for lib in self.libraries],
                "function":
                    f'''{self.function_name} <- function() {{
                        return()
                    }}''',
                "list":
                    f'''{self.class_name} <- list()''',
                "variable":
                    f'''{self.variable_name} <- 0'''
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
            "./", now.strftime("%YY%mm%dd_%HH%MM%SS"), self.file_extension
        ])
        if verbose == True:
            print("Modified filetype to " + self.file_type)

    # read config dictionary & set values
    def from_config(self, config_dict, verbose=True):
        # check if config_dict["type"] ==  "markdown"
        if config_dict["type"] != "markdown":
            raise TypeError("type should be markdown")
        # set values
        self.metadata["Description"] = config_dict["description"]
        self.intro_sentence = config_dict["description"]
        self.path = config_dict["path"]
        self.title = config_dict["title"]
        self.subtitles = config_dict["subtitles"]
        if verbose == True:
            print("Config file loaded: " + config_dict["name"])

    def generate_contents():
        # TODO: FILL IN THIS FUNCTION
        pass

    def write(self, new_contents=True, save=True, verbose=True):
        if new_contents == True:
            md_contents = self.generate_contents(set_contents=True)

        make_basedir(self.path)

        md_file = open(self.path, "w")
        md_file.write(self.contents)
        md_file.close()
        if verbose == True:
            print("Successfully generated: " + self.path)
        pass
