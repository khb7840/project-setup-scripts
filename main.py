# python3 code

import sys
import pkg_resources

from generator.markdown_generator import MarkdownGenerator
from generator.yaml_parser import YamlParser
from generator.script_generator import ScriptGenerator, update_script_info
from generator.dir_generator import DirGenerator, make_basedir

if len(sys.argv) == 1:
    CONFIG_PATH = pkg_resources.resource_filename(
        "generator", "default_structure.yaml"
    )
else:
    CONFIG_PATH = sys.argv[1]

config = YamlParser(CONFIG_PATH)

dir_gen = DirGenerator()

for dirconf in config.dir_list:
    dir_gen.from_config(dirconf)
    dir_gen.write()

for fileconf in config.file_list:
    if fileconf["type"] == "markdown":
        md_gen = MarkdownGenerator()
        md_gen.from_config(fileconf)
        md_gen.write()
    else:
        sc_gen = ScriptGenerator()
        sc_gen.from_config(fileconf)
        sc_gen.write()

print("DONE")
