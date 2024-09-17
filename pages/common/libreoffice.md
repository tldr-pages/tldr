# libreoffice

> CLI for the powerful and free office suite LibreOffice.
> More information: <https://www.libreoffice.org/>.

- Open one or more files in read-only mode:

`libreoffice --view {{path/to/file1 path/to/file2 ...}}`

- Display the content of one or more files:

`libreoffice --cat {{path/to/file1 path/to/file2 ...}}`

- Print files using a specific printer:

`libreoffice --pt {{printer_name}} {{path/to/file1 path/to/file2 ...}}`

- Convert all `.doc` files in current directory to PDF:

`libreoffice --convert-to {{pdf}} {{*.doc}}`
