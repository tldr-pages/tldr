# ed

> The original Unix text editor.
> More information: <https://www.gnu.org/software/ed/manual/ed_manual.html>.

- Start ed, editing an empty document (which can be saved as a new file in the current directory):

`ed`

- Start ed, editing an empty document, with `:` as a command prompt indicator:

`ed -p :`

- Start ed editing an existing file (this shows the byte count of the loaded file):

`ed -p : {{path/to/file}}`

- Toggle the printing of error explanations. (By default, explanations are not printed and only a `?` appears):

`H`

- Add text to the current document. Mark completion by entering a period by itself in a new line:

`a<Enter>{{text_to_insert}}<Enter>.`

- Print the entire document (`,` is a shortcut to the range `1,$` which covers the start to the end of the document):

`,p`

- Write the current document to a new file (the filename can be omitted if `ed` was called with an existing file):

`w {{filename}}`

- Quit ed:

`q`
