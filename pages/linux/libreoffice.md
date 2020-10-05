# libreoffice

> Use the powerful and free office suite, LibreOffice, from the command line.
> More information: <https://www.libreoffice.org/>.

- Open the given files in viewer mode (read-only):

`libreoffice --view {{file1}} {{file2}} {{file3}}`

- Display the content of specific files:

`libreoffice --cat {{path/to/file1}} {{path/to/file2}}`

- Print the given files to a given printer:

`libreoffice --pt {{printer_name}} {{file1}} {{file2}}`

- Convert all .doc files in current directory to pdf:

`libreoffice --convert-to {{pdf}} {{*.doc}}`
