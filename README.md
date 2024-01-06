# dir tree

dir tree is a Python package designed to process hierarchical structures such as directory trees or JSON files. It provides functionalities to visualize the structure as a tree, search for specific nodes, and filter nodes based on custom criteria. 

Input: JSON/dictionary/github directory
Output: String 

Features:
Input:
    JSON : format 
    Dictioanary:
    Github directory: etc 



# USAGE 

## Basic Usage 

### Input: Dictionary/JSON

```
from dir_tree import format_tree, search_node, filter_nodes

# Define your structure
structure = {
    "root": ["child1", "child2"],
    "child1": ["grandchild1", "grandchild2"],
    "child2": ["grandchild3"],
}

# Visualize the structure
print(format_tree(structure))

# Search for a node
print(search_node(structure, "target_node"))

# Filter nodes
filtered_structure = filter_nodes(structure, lambda node: "grandchild" in node)
print(format_tree("root", filtered_structure))
```

### Input: Using Github personal access tokens

```
from github import Github, Auth

from dir_tree import format_tree, search_node, filter_nodes


# Authentication and GitHub Initialization
token = ''
auth = Auth.Token(token)
g = Github(auth=auth)


# Visulise the repo
print(format_tree(git_tree(g, repo_name)))


# Search for a file and return the file path
print(search_node(git_tree(g, repo_name), "file_name"))
```


# Installation 
```
pip3 install dir_tree
```


# Where to Use
dir_tree is ideal for:

- Visualizing many git repos. 
- Building CLI tools that require tree-structure 
- Including gile structures in HTML. Since we return a string we can wrap the file structure with 
```<pre> </pre>``` to show in the html

# Contributing
Contributions to dir tree are welcome! Please follow these steps to contribute:

- Fork the repository.
- Create a new branch for your feature or fix.
- Commit your changes.
- Push to the branch.
- Submit a pull request.

Or otherwise please make an Issue!


# License
This project is licensed under the MIT License.


