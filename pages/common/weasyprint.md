# weasyprint

> Render HTML to PDF or PNG.
> More information: <https://weasyprint.org/>.

- Render a HTML file to PDF:

`weasyprint {{path/to/input.html}} {{path/to/output}}.pdf`

- Render a HTML file to PNG, including an additional user stylesheet:

`weasyprint {{path/to/input.html}} {{path/to/output}}.png --stylesheet {{path/to/stylesheet.css}}`

- Output additional debugging information when rendering:

`weasyprint {{path/to/input.html}} {{path/to/output}}.pdf --verbose`

- Specify a custom resolution when outputting to PNG:

`weasyprint {{path/to/input.html}} {{path/to/output}}.png --resolution {{300}}`

- Specify a base url for relative urls in the input HTML file:

`weasyprint {{path/to/input.html}} {{path/to/output}}.png --base-url {{url_or_filename}}`
