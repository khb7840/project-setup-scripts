# python3 script
# A script to generate a markdown document
# USAGE: python new_markdown_doc.py <FILE_NAME>

import os
import sys
import datetime

# Check the number of arguments
if len(sys.argv) < 2:
    print("Name of your documents should be supplied.")
    sys.exit()
elif len(sys.argv) == 2:
    SUBTITLES = ["Introduction", "Body paragraphs", "Conclusion"]
    EX_CONTENTS = ["Introductory contents",
                   "Main contents", "Conclusive paragraphs"]
else:
    SUBTITLES = sys.argv[2:]
    EX_CONTENTS = [title + " contents" for title in SUBTITLES]

# GLOBAL VARIABLES
# 00. MD PATH: a path for markdown documents
MD_TITLE = str(sys.argv[1])
MD_PATH = "./" + MD_TITLE + ".md"
# Basic information
# 01. AUTHOR INFO
AUTHOR_INFO = "Hyunbin Kim (khb7840@gmail.com)"
# 02. TIMETAG
now = datetime.datetime.now()
TIMETAG = now.strftime("%Y. %m. %d. %H:%M:%S")


def generate_md_contents(markdown_path):
    contents_lines = []
    # Metadata in YAML
    contents_lines.append("---")
    contents_lines.append("```yaml")
    contents_lines.append("Title: " + MD_TITLE)
    contents_lines.append("Author: " + AUTHOR_INFO)
    contents_lines.append("Date: " + TIMETAG)
    contents_lines.append("```")
    contents_lines.append("---")
    contents_lines.append("")

    # Title: H1
    contents_lines.append("# " + MD_TITLE)
    contents_lines.append("A markdown documents titled " + MD_TITLE)
    contents_lines.append("")

    # Table of contents
    contents_lines.append("---")
    contents_lines.append("# Table of contents")
    # Append subtitles to table of contents
    # FORMAT: 1. [Sometitle](#sometitle)
    for i, subtitle in enumerate(SUBTITLES):
        lsub = subtitle.lower()
        contents_lines.append(str(i+1) + ". [" + subtitle + "](#" + lsub + ")")
    contents_lines.append("---")
    contents_lines.append("")

    # Main body
    for i in range(len(SUBTITLES)):
        contents_lines.append("## " + SUBTITLES[i])
        contents_lines.append(EX_CONTENTS[i] + " comes here")

    return "\n".join(contents_lines)


def main():
    # Check if a file exists at MD_PATH
    # If true, generate MD_TITLE.md
    if os.path.isfile(MD_PATH):
        print("File already exists: " + MD_TITLE + ".md")
        sys.exit()
    else:
        md_contents = generate_md_contents(MD_TITLE)
        md_file = open(MD_PATH, "w")
        md_file.write(md_contents)
        md_file.close()
        print("Successfully generated: " + MD_TITLE + ".md")


if __name__ == "__main__":
    main()
