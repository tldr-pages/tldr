# aha

> Convert ANSI escape codes to HTML.
> More information: <https://github.com/theZiz/aha>.

- Convert a file's ANSI escapes to HTML:

`aha --file {{path/to/file.txt}}`

- Convert ANSI escapes from `stdin` to HTML:

`{{command_with_ansi_output}} | aha`

- Convert output to HTML and save it:

`{{command}} | aha > {{path/to/output.html}}`

- Convert with a custom HTML title:

`{{command}} | aha --title "{{My custom title}}"`
