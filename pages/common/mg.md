# mg

> A small, fast, portable text editor.
> Based on `emacs`.
> More information: <https://github.com/hboetes/mg>.

- Open a file for editing:

`mg {{path/to/file}}`

- Open a file at a specified line number:

`mg +{{line_number}} {{path/to/file}}`

- Open files read-only for viewing:

`mg -R {{path/to/file1 path/to/file2 ...}}`

- Disable `~` backup files while editing:

`mg -n {{path/to/file}}`
