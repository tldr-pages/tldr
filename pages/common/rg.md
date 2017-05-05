# ripgrep

> A fast command-line search tool.

- Recursively search the current directory for a regex pattern:

`rg {{pattern}}`

- Search for pattern including all .gitignored and hidden files:

`rg -uu {{pattern}}`

- Search for a pattern only in a certain filetype (e.g., html, css, etc.):

`rg -t {{filetype}} {{pattern}}`

- Search for a pattern only in a subset of directories:

`rg {{pattern}} {{set_of_subdirs}}`

- Search for a pattern in files matching a glob (e.g., `README.*`):

`rg {{pattern}} -g {{glob}}`
