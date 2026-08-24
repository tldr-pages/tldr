# aha

> Convert ANSI escape sequences to HTML.
> More information: <https://manned.org/aha>.

- Convert terminal output to HTML:

`{{color_command}} | aha > {{path/to/output}}.html`

- Read from a file instead of `stdin`:

`aha -f {{path/to/input.txt}} > {{path/to/output}}.html`

- Convert to HTML with a black background:

`{{color_command}} | aha {{[-b|--black]}} > {{path/to/output}}.html`

- Convert to HTML with a pink background and set the document title:

`{{color_command}} | aha {{[-p|--pink]}} {{[-t|--title]}} "{{title}}" > {{path/to/output}}.html`

- Add a CSS file to the HTML output:

`{{color_command}} | aha {{[-c|--css]}} {{path/to/style}}.css > {{path/to/output}}.html`

- Enable word-wrap to prevent horizontal scrolling:

`{{color_command}} | aha {{[-w|--word-wrap]}} > {{path/to/output}}.html`

- Display help:

`aha {{[-h|--help]}}`
