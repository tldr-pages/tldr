# gf

> A wrapper around `grep` to help you find specific patterns in files or text streams.
> More information: <https://github.com/tomnomnom/gf>

- List all available patterns:
  gf -list

- Search for a specific pattern in a file or directory:
  gf {{pattern_name}} {{path/to/file_or_directory}}

- Search using a pattern from `stdin` (pipe):
  cat {{path/to/file}} | gf {{pattern_name}}

- Display the raw regular expression for a specific pattern:
  gf -dump {{pattern_name}}

- List the directory where `gf` looks for its JSON pattern definitions:
  ls {{~/.gf}}
