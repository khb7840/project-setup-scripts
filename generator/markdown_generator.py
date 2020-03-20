# python3 code
# Modified from new_markdown_doc.py
# Author: Hyunbin Kim

# import necessary libraries
import os
import sys
import datetime
import collections
from generator.dir_generator import make_basedir


class MarkdownGenerator:
    # check variables & initialization
    def __init__(self, title=""):
        # Get timetag
        now = datetime.datetime.now()
        self.timetag = now.strftime("%Y. %m. %d. %H:%M:%S")

        # If title is not given in constructor,
        # use timetag string as title
        if title == "":
            timetag_title = now.strftime("%Y%m%d_%H%M%S")
            self.title = timetag_title
        else:
            self.title = title

        # markdown file path: "./{TITLE}.md"
        self.type = "markdown"
        self.path = "./" + self.title + ".md"

        # Setting author info
        self.author = "Hyunbin Kim"
        self.email = "khb7840@gmail.com"
        self.author_info = self.author + "(" + self.email + ")"

        # default subtitles: [(subtitle1, contents1), ...]
        self.subtitles = ["Introduction", "Body", "Conclusion"]

        # other parameters
        self.prefix_title = "#"
        self.prefixs_subtitle = "##"
        self.horizontal_line = "---"
        self.intro_sentence = "A markdown documents titled " + self.title
        self.toc = "## Table of contents"
        self.suffix_contents = "comes here"

        # metadata
        self.metadata = collections.OrderedDict({
            "Title": self.title, "Author": self.author_info,
            "Date": self.timetag, "Description": "A markdown document"
        })

        # contents
        self.contents = ""

    # set new title
    def set_title(self, title):
        self.title = title
        self.path = "./" + self.title + ".md"

    # set new path
    def set_path(self, path):
        self.path = path

    # set author information
    def set_author_info(self, author, email):
        self.author = author
        self.email = email
        self.author_info = author + "(" + email + ")"

    # set subtitles
    def set_subtitles(self, *args):
        new_subtitles = [arg for arg in args]
        self.subtitles = new_subtitles

    # set contents
    def set_contents(self, contents_string):
        self.contents = contents_string

    # append new item in metadata
    def append_metadata(self, key, value):
        self.metadata[key] = value

    # generate_contents: returns string with generated markdown contents
    def generate_contents(self, metadata=True, set_contents=True):
        # Empty list to save contents line by line
        contents_lines = []

        # If metadata == True, save metadata in yaml format
        if metadata == True:
            contents_lines.append(self.horizontal_line)
            contents_lines.append("```yaml")

            # iterate with metadata
            for item in self.metadata.items():
                contents_lines.append(item[0] + ": " + item[1])

            contents_lines.append("```")
            contents_lines.append(self.horizontal_line)
            contents_lines.append("")

        # Title
        contents_lines.append(self.prefix_title + " " + self.title)
        contents_lines.append(self.intro_sentence)
        contents_lines.append("")

        # Table of contents
        contents_lines.append(self.horizontal_line)
        contents_lines.append(self.toc)
        # FORMAT: 1. [Sometitle](#sometitle)
        for i, subtitle in enumerate(self.subtitles):
            lsub = subtitle.lower()
            contents_lines.append(
                str(i+1) + ". [" + subtitle + "](#" + lsub + ")"
            )
        contents_lines.append(self.horizontal_line)
        contents_lines.append("")

        # Main body
        for subtitle in self.subtitles:
            contents_lines.append(self.prefixs_subtitle + " " + subtitle)
            contents_lines.append(subtitle + " " + self.suffix_contents)

        # Set self.contents
        generated_contents = "\n".join(contents_lines)
        if set_contents == True:
            self.contents = generated_contents

        return generated_contents

    # write: save contents to path
    def write(self, new_contents=True, save=True, verbose=True):
        if new_contents == True:
            md_contents = self.generate_contents(set_contents=True)

        make_basedir(self.path)

        md_file = open(self.path, "w")
        md_file.write(self.contents)
        md_file.close()
        if verbose == True:
            print("Successfully generated: " + self.path)

    # read config dictionary & set values
    def from_config(self, config_dict, verbose=True):
        # check if config_dict["type"] ==  "markdown"
        if config_dict["type"] != "markdown":
            raise TypeError("type should be markdown")
        # set values
        self.intro_sentence = config_dict["description"]
        self.path = config_dict["path"]
        self.title = config_dict["title"]
        self.subtitles = config_dict["subtitles"]
        self.metadata["Description"] = config_dict["description"]
        self.metadata["Title"] = config_dict["title"]
        if verbose == True:
            print("Config file loaded: " + config_dict["path"])
