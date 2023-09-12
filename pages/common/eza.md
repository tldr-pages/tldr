# eza

> Modern, maintained replacement for `ls`, built on `exa`.
> More information: <https://github.com/eza-community/eza>.

- List files one per line:

`eza --oneline`

- List all files, including hidden files:

`eza --all`

- Long format list (permissions, ownership, size and modification date) of all files:

`eza --long --all`

- List files with the largest at the top:

`eza --reverse --sort={{size}}`

- Display a tree of files, three levels deep:

`eza --long --tree --level={{3}}`

- List files sorted by modification date (oldest first):

`eza --long --sort={{modified}}`

- List files with their headers, icons, and Git statuses:

`eza --long --header --icons --git`

- Don't list files mentioned in `.gitignore`:

`eza --git-ignore`
