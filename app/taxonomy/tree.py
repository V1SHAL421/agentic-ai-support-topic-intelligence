from typing import List

from app.schemas.taxonomy_data import TaxonomyData, TaxonomyOutput

class Node:
    def __init__(self, value: str, children: List | None = None):
        self.value = value
        self.children = children or []

class TaxonomyTree:
    def __init__(self, taxonomy_data: dict | TaxonomyData | None):
        self.root = Node("Customer Support Topics")
        if taxonomy_data:
            if isinstance(taxonomy_data, dict):
                taxonomy_data = TaxonomyData(**taxonomy_data)
            self._build_tree(taxonomy_data)

    def _build_tree(self, data: TaxonomyData, parent=None):
        if parent is None:
            parent = self.root
        
        for primary, secondaries in data.primary_to_secondary_data.items():
            primary_node = Node(primary)
            parent.children.append(primary_node)

            for secondary in secondaries:
                secondary_node = Node(secondary)
                primary_node.children.append(secondary_node)

                tertiary = data.secondary_to_tertiary_data.get(secondary, [])
                for tertiary_item in tertiary:
                    tertiary_node = Node(tertiary_item)
                    secondary_node.children.append(tertiary_node)

    def validate_path(self, llm_output: TaxonomyOutput) -> bool:
        primary_node = next(node for node in self.root.children if node.value == llm_output.primary_topic)
        if not primary_node:
            # raise ValueError(f"Primary topic '{llm_output.primary_topic}' not found in the tree.")
            return False
        secondary_node = next((node for node in primary_node.children if node.value == llm_output.secondary_topic), None)
        if not secondary_node:
            # raise ValueError(f"Secondary topic '{llm_output.secondary_topic}' not found under primary topic '{llm_output.primary_topic}'.")
            return False
        tertiary_node = next((node for node in secondary_node.children if node.value == llm_output.tertiary_topic), None)
        if not tertiary_node:
            # raise ValueError(f"Tertiary topic '{llm_output.tertiary_topic}' not found under secondary topic '{llm_output.secondary_topic}'.")
            return False
        return True
        

        

    
    

    