from typing import List
import xml.etree.ElementTree as ET


class XMLParser:
    def __init__(self, file_path):
        self.tree = ET.parse(file_path)
        self.root = self.tree.getroot()

    def get(self, element_name) -> List[str]:
        data = []

        for element in self.root.iter(element_name):
            data.append(element.text)

        return data

