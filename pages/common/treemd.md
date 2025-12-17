# treemd

> A modern markdown viewer combining tree-based navigation with interactive TUI.
> More information: <https://github.com/Epistates/treemd>.

- Open a markdown file in interactive TUI mode:

`treemd {{path/to/file.md}}`

- List all headings in a markdown file:

`treemd --list {{path/to/file.md}}`

- Show the heading tree structure of a markdown file:

`treemd --tree {{path/to/file.md}}`

- Extract a specific section by heading name:

`treemd --section {{heading_name}} {{path/to/file.md}}`

- Filter headings by a specific pattern:

`treemd --list --filter {{pattern}} {{path/to/file.md}}`

- Set up shell completions:

`treemd --setup-completions`
