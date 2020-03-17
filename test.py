# python3 code

from generator.markdown_generator import MarkdownGenerator
from generator.yaml_parser import YamlParser

test_mdg = MarkdownGenerator(title="TEST_TOY")
# test_mdg.write()

test_yaml = YamlParser("./generator/default_structure.yaml")


test_mdg.from_config(test_yaml.file_list[0])
test_mdg.write()
