# fzf 
> A command-line fuzzy finder.
> More information: <https://github.com/junegunn/fzf>.

- Start fzf on all files in the current directory and subdirectories:

`fzf`

- Start fzf on all running processes:

`ps aux | fzf`

- Select multiple files with TAB and write them to a file:

`find . -type f | fzf --multi > {{filename}}`

- Start fzf with a specified query:

`fzf --query "{{query}}"`

- Start fzf on entries that start with core and end with either .go or .rb:

`fzf --query "^core.*\.(go|rb)$"`

- Start fzf with case-insensitive search:

`fzf --case-insensitive`

- Start fzf in reverse layout (top-down instead of bottom-up):

`fzf --reverse`