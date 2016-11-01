# ripgrep (rg)

> A fast commandline search tool.

- Recursively search the current directory for a regex pattern:

`rg {{pattern}}`

- Search in all .gitignored and hidden files:

`rg -uu {{pattern}}`

- Search only in html or css files for a pattern:

`rg -thtml -tcss {{pattern}}`

- Only search for a pattern in files matching a glob (e.g., 'README.*'):

`rg {{pattern}} -g {{glob}}`
