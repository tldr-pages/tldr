# exa

> A modern replacement for `ls` (List directory contents).
> Note: `exa` is no longer maintained. Use `eza` instead.
> See also: `eza`.
> More information: <https://github.com/ogham/exa#command-line-options>.

- List files one per line:

`exa {{[-1|--oneline]}}`

- List all files, including hidden files:

`exa {{[-a|--all]}}`

- List all files in long format (permissions, ownership, size, and modification date):

`exa {{[-l|--long]}} {{[-a|--all]}}`

- List files with the largest at the top:

`exa {{[-r|--reverse]}} {{[-s|--sort]}} {{size}}`

- Display a tree of files, three levels deep:

`exa {{[-l|--long]}} {{[-T|--tree]}} {{[-L|--level]}} {{3}}`

- List files sorted by modification date (oldest first):

`exa {{[-l|--long]}} {{[-s|--sort]}} {{modified}}`

- List files with their headers, icons, and Git statuses:

`exa {{[-l|--long]}} {{[-h|--header]}} --icons --git`

- Don't list files mentioned in `.gitignore`:

`exa --git-ignore`
