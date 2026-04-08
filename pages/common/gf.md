# gf

> A wrapper around `grep` to help you find specific patterns in files or text streams.
> More information: <https://github.com/tomnomnom/gf>

- List all available patterns:

  `gf {{-list}}`

- Search for a specific pattern in a file or directory:

  `gf {{pattern_name}} {{path/to/file_or_directory}}`

- Search for a pattern using `stdin` (pipe):
  
  `cat {{path/to/file}} | gf {{pattern_name}}`

- Display the raw regular expression (regex) for a specific pattern:
  
  `gf {{-dump}} {{pattern_name}}`

- List the directory where `gf` looks for its JSON pattern definitions:
  
  `ls {{~/.gf}}`

- Combine `gf` with other tools to find interesting parameters in URLs:
  
  `cat {{urls.txt}} | gf {{interestingparams}}`
