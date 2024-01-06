from main import *
from github import Github, Auth

sample_structure = {
    "root": ["child1", "child2"],
    "child1": ["grandchild1", "grandchild2"],
    "child2": ["grandchild3"],
    "grandchild1": [],
    "grandchild2": [],
    "grandchild3": []
}

# Testing the functions
filtered_structure = filter(sample_structure, lambda node: "grandchild" in node)
filtered_tree = format_tree(filtered_structure)
search_result = search(sample_structure, "grandchild2")
tree_with_info = format_tree_info("root", sample_structure)
directory_tree = format_tree(sample_structure)

result_string = f"\nFilter Test:\n{filtered_tree}\nSearch Test:\n{search_result}\nTree with Node Information:\n{tree_with_info}\nDirectory Structure:\n{directory_tree}"
print(result_string)


# Authentication and GitHub Initialization
token = ''
print(token)
auth = Auth.Token(token)
print(auth)
g = Github(auth=auth)
print(g)


# Visulise the repo
print(format_tree(git_tree(g, 'mori.css')))