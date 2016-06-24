# xclip

> Copy STDIN to clipboard or print clipboard to STDOUT.

- Copy output to clipboard:

`echo 123 | xclip -i`

- Copy output to system clipboard:

`echo 123 | xclip -sel clip`

- Paste clipboard:

`xclip -o > file.txt`
