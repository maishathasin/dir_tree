import json
import os



# Function to format tree with info with children and depth
def format_tree_info( structure,node='root', prefix="", depth=0, is_last=True):

    tree = ""
    num_children = len(structure.get(node, []))
    tree += f"{prefix}{'└── ' if is_last else '├── '}{node.split('/')[-1]} (Children: {num_children}, Depth: {depth})\n"
    
    if node in structure:
        children = structure[node]
        for i, child in enumerate(children):
            extension = "    " if is_last else "│   "
            tree += format_tree_info(child, structure, prefix + extension, depth + 1, i == len(children) - 1)
    return tree


# function to search for a file/folder, returns a string 
# cannot search in hidden files
def search(structure, target):
    path = []

    def find_path(node, target):
        if node == target:
            return True
        if node in structure:
            for child in structure[node]:
                path.append(child)
                if find_path(child, target):
                    return True
                path.pop()
        return False

    for root in structure:
        path.append(root)
        if find_path(root, target):
            return ' -> '.join(path)
        path.pop()
    return "Node not found"

# Function to create filters for the tree, criteria boolean function 
# see test.py for examples for usage
def filter(structure, criteria):
    filtered_structure = {}

    def find_parents(child_node, parents):
        for node, children in structure.items():
            if child_node in children:
                parents.append(node)
                find_parents(node, parents)
        return parents

    for node in structure:
        if criteria(node):
            parents = find_parents(node, [])
            for parent in parents:
                if parent not in filtered_structure:
                    filtered_structure[parent] = []
                if node not in filtered_structure:
                    filtered_structure[node] = []
                if node not in filtered_structure[parent]:
                    filtered_structure[parent].append(node)

    return {k: v for k, v in filtered_structure.items() if k in structure}

# basic format trees without any info
def format_tree(structure):
    def format_tree(node, prefix="", is_last=True):
        tree = ""
        if node:  
            tree += f"{prefix}{'└── ' if is_last else '├── '}{node.split('/')[-1]}\n"

        if node in structure:
            children = structure[node]
            for i, child in enumerate(children):
                extension = "    " if is_last else "│   "
                tree += format_tree(child, prefix + extension, i == len(children) - 1)
        return tree

    roots = [node for node in structure if not any(node in items for items in structure.values())]
    tree = ""
    for i, root in enumerate(roots):
        tree += format_tree(root, is_last=(i == len(roots) - 1))
    return tree.strip()



# For git repos, returns a dictionary of the folders
def git_tree(g, repo_name):
    repo = g.get_user().get_repo(repo_name)
    contents = repo.get_contents("")
    directory_structure = {"root": []}

    def parse_contents(contents, parent_path="root"):
        for content in contents:
            relative_path = f"{parent_path}/{content.name}" if parent_path != "root" else content.name

            if content.type == "dir":
                directory_structure[parent_path].append(relative_path)
                directory_structure[relative_path] = []
                try:
                    subdir_contents = repo.get_contents(content.path)
                    parse_contents(subdir_contents, relative_path)
                except Exception as e:
                    print(f"Error accessing directory {relative_path}: {e}")
            else:
                directory_structure[parent_path].append(relative_path)
                directory_structure[relative_path] = []

    parse_contents(contents)
    return directory_structure

