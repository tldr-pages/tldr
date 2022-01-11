# clifm

> The command line file manager.
> More information: <https://github.com/leo-arch/clifm>.

- Change to/open the file whose ELN (entry list number) is 12 (ELN can be replaced by the actual file name, e.g. `/etc`):

`12`

- Create a new file and a new directory:

`n file dir/`

- Go back and forth in the directory history list:

<kbd>Shift-Left</kbd> (or <kbd>Alt-j</kbd>) / <kbd>Shift-Right</kbd> (or <kbd>Alt-k</kbd>)

- Select all PNG files in the current directory: 

`s *.png`

- Search for PDF files in the current directory:

`/*.pdf`

- Remove the file whose ELN is 24 (use `t` to trash the file instead):

`r 24`

- Copy selected files into the current directory:

`c sel`

- Open the bookmarks screen:

`bm` (or <kbd>Alt-b</kbd>)
