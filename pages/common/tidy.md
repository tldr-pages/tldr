# tidy

> Clean up and pretty print HTML, XHTML and XML files.
> Note: `tidy` cannot preserve original indentation.
> More information: <https://api.html-tidy.org/tidy/tidylib_api_next/group__options__cli.html#gad7a9fcaf7b2a712a82e625e84c042b28>.

- Pretty print an HTML file:

`tidy {{path/to/file.html}}`

- Enable indentation, wrapping lines in 100, saving to `output.html`:

`tidy {{[-i|--indent]}} y {{[-w|--wrap]}} 100 {{[-o|-output]}} {{path/to/output.html}} {{path/to/file.html}}`

- Modify an HTML file in-place using a configuration file:

`tidy -config {{path/to/configuration}} {{[-m|-modify]}} {{path/to/file.html}}`
