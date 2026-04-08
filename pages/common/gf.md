# gf

> A wrapper around `grep` to help you find specific patterns in files or text streams.
> More information: <https://github.com/tomnomnom/gf>.

- List all available patterns:

`gf {{-list}}`

- Search for a specific pattern in a file or directory:

`gf {{pattern_name}} {{path/to/file}}`

- Search for a pattern using `stdin`:

`cat {{file}} | gf {{pattern_name}}`

- Display the raw `regex` for a specific pattern:

`gf {{-dump}} {{pattern_name}}`

- Combine `gf` with other tools to find interesting parameters in URLs:

`cat {{urls.txt}} | gf {{interestingparams}}`
