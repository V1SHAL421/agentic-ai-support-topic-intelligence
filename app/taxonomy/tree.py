from typing import List

from app.schemas.taxonomy_data import TaxonomyData

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

    
    

    