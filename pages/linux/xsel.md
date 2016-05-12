# xsel

> Selection manipulation tool.
> For example, xsel can copy STDIN to clipboard, or print clipboard to STDOUT.

- Copy output to clipboard:

`echo 123 | xclip -bi`

- Paste clipboard:

`xsel -bo > file.txt`

- Clear the clipboard:

`xsel -bc`
