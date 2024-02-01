# textutil

> Used to manipulate text files of various formats.
> More information: <https://keith.github.io/xcode-man-pages/textutil.1.html>.

- Display information about `foo.rtf`:

`textutil -info {{path/to/foo.rtf}}`

- Convert `foo.rtf` into `foo.html`:

`textutil -convert {{html}} {{path/to/foo.rtf}}`

- Convert rich text to normal text:

`textutil {{path/to/foo.rtf}} -convert {{txt}}`

- Convert `foo.txt` into `foo.rtf`, using Times 10 for the font:

`textutil -convert {{rtf}} -font {{Times}} -fontsize {{10}} {{path/to/foo.txt}}`

- Load all RTF files in the current directory, concatenates their contents, and writes the result out as `index.html` with the HTML title set to "Several Files":

`textutil -cat {{html}} -title "Several Files" -output {{path/to/index.html}} *.rtf`
