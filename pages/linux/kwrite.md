# kwrite

> Text editor of the KDE Desktop project.
> See also `kate`.
> More information: <https://docs.kde.org/stable5/en/kate/kwrite/command-line-options.html>.

- Open a text file:

`kwrite {{path/to/file}}`

- Open multiple text files:

`kwrite {{file1 file2 ...}}`

- Open a text file with a specific encoding:

`kwrite --encoding {{UTF-8}} {{path/to/file}}`

- Open a text file and navigate to a specific line and column:

`kwrite --line {{line_number}} --column {{column_number}} {{path/to/file}}`
