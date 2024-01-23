# vidir

> Edit directories in a text editor.
> More information: <https://joeyh.name/code/moreutils/>.

- Edit the contents of the specified directories:

`vidir {{path/to/directory1 path/to/directory2 ...}}`

- Edit the contents of current directory:

`vidir`

- Read a list of files to edit from `stdin`:

`{{command}} | vidir -`
