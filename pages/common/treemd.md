# treemd

> A markdown viewer combining tree-based navigation with interactive TUI.
> More information: <https://github.com/Epistates/treemd#usage>.

- Open a markdown file in interactive TUI mode:

`treemd {{path/to/file}}.md`

- List all headings in a markdown file:

`treemd {{[-l|--list]}} {{path/to/file}}.md`

- Show the heading tree structure of a markdown file:

`treemd --tree {{path/to/file}}.md`

- Extract a specific section by heading name:

`treemd {{[-s|--section]}} {{heading_name}} {{path/to/file}}.md`

- Filter headings by a specific pattern:

`treemd {{[-l|--list]}} --filter {{pattern}} {{path/to/file}}.md`

- Query and extract markdown structure using the treemd query language:

`treemd {{[-q|--query]}} '{{.h2 | text}}' {{path/to/file}}.md`
