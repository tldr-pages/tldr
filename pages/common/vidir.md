# vidir

> Edit directories in a text editor.
> More information: <https://manned.org/vidir>.

- Edit the contents of the specified directories:

`vidir {{path/to/directory1 path/to/directory2 ...}}`

- Display each action taken by the program:

`vidir {{[-v|--verbose]}} {{path/to/directory1 path/to/directory2 ...}}`

- Edit the contents of current directory:

`vidir`

- Use the specified text editor:

`EDITOR={{vim}} vidir {{path/to/directory1 path/to/directory2 ...}}`

- Read a list of files to edit from `stdin`:

`{{command}} | vidir -`
