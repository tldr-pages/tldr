# aha

> Convert ANSI escape sequences to HTML.
> More information: <https://manned.org/aha>.

- Convert terminal output to HTML:

`{{command_with_color_output}} | aha > {{path/to/output.html}}`

- Read from a file instead of `stdin`:

`aha -f {{path/to/input.txt}} > {{path/to/output.html}}`

- Convert to HTML with a black background:

`{{command_with_color_output}} | aha {{[-b|--black]}} > {{path/to/output.html}}`

- Convert to HTML with a pink background and set the document title:

`{{command_with_color_output}} | aha {{[-p|--pink]}} {{[-t|--title]}} "{{title}}" > {{path/to/output.html}}`

- Add a CSS file to the HTML output:

`{{command_with_color_output}} | aha {{[-c|--css]}} {{path/to/style.css}} > {{path/to/output.html}}`

- Enable word-wrap to prevent horizontal scrolling:

`{{command_with_color_output}} | aha {{[-w|--word-wrap]}} > {{path/to/output.html}}`

- Display help:

`aha {{[-h|--help]}}`
