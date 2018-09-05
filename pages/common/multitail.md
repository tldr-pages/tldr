# multitail

> Monitor last part of multiple files in multiple windows in a terminal.

- Monitor two files in two separate windows:

`multitail {{file1}} {{file2}}`

- Merge two files in one window:

`multitail {{file1}} -I {{file2}}`

- Show two files in two windows side by side:

`multitail -s {{file1}} {{file2}}`

- Show output of two commands:

`multitail -l "ping {{host1}}" -l "ping {{host1}}"`
