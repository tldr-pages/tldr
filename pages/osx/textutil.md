# textutil

> Manipulate text files of various formats.
> More information: <https://keith.github.io/xcode-man-pages/textutil.1.html>.

- Display information about `file.rtf`:

`textutil -info {{path/to/file.rtf}}`

- Convert `file.rtf` into `file.html`:

`textutil -convert html {{path/to/file.rtf}}`

- Convert rich text to normal text:

`textutil {{path/to/file.rtf}} -convert txt`

- Convert `file.txt` into `file.rtf`, using Times 10 for the font:

`textutil -convert rtf -font Times -fontsize 10 {{path/to/file.txt}}`

- Load all RTF files in the current directory, concatenates their contents, and writes the result out as `index.html` with the HTML title set to "Several Files":

`textutil -cat {{html}} -title "Several Files" -output {{path/to/index.html}} *.rtf`
