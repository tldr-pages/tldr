# nkf

> Convert character code and new line code.

- Stdout utf-8 code:

`nkf -w {{path/to/file.txt}}`

- Stdout shift_jis code:

`nkf -s {{path/to/file.txt}}`

- Overwrite as utf-8 code:

`nkf -w --overwrite {{path/to/file.txt}}`

- Set new line code to LF and overwrite (unix type):

`nkf -d --overwrite {{path/to/file.txt}}`

- Set new line code to CRLF and overwrite (windows type):

`nkf -c --overwrite {{path/to/file.txt}}`

- Decrypt mime file and overwrite:

`nkf -m --overwrite {{path/to/file.txt}}`
