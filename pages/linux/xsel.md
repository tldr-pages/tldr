# xsel

> Selection manipulation tool.
> For example, xsel can copy STDIN to clipboard, or print clipboard to STDOUT.

- Clipboard selection:

`-b or --clipboard`

- Primary selection:

`-p or --primary`

- Secondary selection:

`-s or --secondary`

- Copy output of a command into the clipboard:

`echo 123 | xsel -bi`

- Copy contents of a file into the clipboard:

`cat {{file}} | xsel -bi`

- Print the clipboard to STDOUT:

`xsel -bo`

- Print the clipboard into a file:

`xsel -bo > {{file}}`

- Clear the clipboard:

`xsel -bc`
