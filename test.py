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

'''
Filter Test:
├── child1
│   ├── grandchild1
│   └── grandchild2
├── root
│   ├── grandchild1
│   ├── grandchild2
│   └── grandchild3
└── child2
    └── grandchild3
Search Test:
root -> child1 -> grandchild2
Tree with Node Information:
└── root (Children: 2, Depth: 0)
    ├── child1 (Children: 2, Depth: 1)
    │   ├── grandchild1 (Children: 0, Depth: 2)
    │   └── grandchild2 (Children: 0, Depth: 2)
    └── child2 (Children: 1, Depth: 1)
        └── grandchild3 (Children: 0, Depth: 2)

Directory Structure:
└── root
    ├── child1
    │   ├── grandchild1
    │   └── grandchild2
    └── child2
        └── grandchild3

'''


# Authentication and GitHub Initialization
token = ''
print(token)
auth = Auth.Token(token)
print(auth)
g = Github(auth=auth)
print(g)

# Visulise the repo
print('output\n',format_tree_info(git_tree(g, 'mori.css')))
'''

└── root (Children: 14, Depth: 0)
    ├── .github (Children: 1, Depth: 1)
    │   └── workflows (Children: 1, Depth: 2)
    │       └── static.yml (Children: 0, Depth: 3)
    ├── LICENSE.txt (Children: 0, Depth: 1)
    ├── README.md (Children: 0, Depth: 1)
    ├── Vintage-cats-2.jpeg (Children: 0, Depth: 1)
    ├── blog.html (Children: 0, Depth: 1)
    ├── blog1.png (Children: 0, Depth: 1)
    ├── blog2.png (Children: 0, Depth: 1)
    ├── docs-pic.png (Children: 0, Depth: 1)
    ├── docs-pic2.png (Children: 0, Depth: 1)
    ├── icon-small.png (Children: 0, Depth: 1)
    ├── index.html (Children: 0, Depth: 1)
    ├── mori.css (Children: 0, Depth: 1)
    ├── mori.min.css (Children: 0, Depth: 1)
    └── package.json (Children: 0, Depth: 1)
'''
# Search for a file and return the file path
# cannot access hidden files
print(search(git_tree(g, 'mori.css'), 'docs-pic.png'))
# return: root -> docs-pic.png

print(search(git_tree(g, 'mori.css'), 'docs-pic.png'))
# basic info 
l = get_info(sample_structure)
print(l)

'''
Total files: 3
Maximum Depth: 2
File type distribution: {'grandchild1': 1, 'grandchild2': 1, 'grandchild3': 1}'''
