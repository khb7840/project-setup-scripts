# python3 code
# parser for yaml with project directory structure
# Author: Hyunbin Kim

# import necessary libraries
import os
import yaml


class YamlParser:
    # check variables & initialization
    def __init__(self, yaml_path):
        # load yaml
        self.yaml_path = yaml_path
        with open(yaml_path, "r") as f:
            self.config_list = yaml.load(f, Loader=yaml.FullLoader)
        self.prefix = self.config_list["prefix"]
        self.dir_list = self.config_list["dir"]
        self.file_list = self.config_list["file"]
        # add prefix to all files & directories
        for dir_dict in self.dir_list:
            dir_dict["path"] = self.prefix + dir_dict["path"]
        for file_dict in self.file_list:
            file_dict["path"] = self.prefix + file_dict["path"]
