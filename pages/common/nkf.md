# nkf

> Network kanji filter.
> Converts kanji code from one encoding to another.
> More information: <https://manned.org/nkf>.

- Convert to UTF-8 encoding:

`nkf -w {{path/to/file.txt}}`

- Convert to SHIFT_JIS encoding:

`nkf -s {{path/to/file.txt}}`

- Convert to UTF-8 encoding and overwrite the file:

`nkf -w --overwrite {{path/to/file.txt}}`

- Use LF as the new line code and overwrite (UNIX type):

`nkf -d --overwrite {{path/to/file.txt}}`

- Use CRLF as the new line code and overwrite (windows type):

`nkf -c --overwrite {{path/to/file.txt}}`

- Decrypt mime file and overwrite:

`nkf -m --overwrite {{path/to/file.txt}}`
