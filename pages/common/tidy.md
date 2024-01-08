# tidy

> Clean up and pretty print HTML, XHTML and XML files.
> NOTE: `tidy` cannot preserve original indentation.
> More information: <https://api.html-tidy.org/tidy/tidylib_api_5.2.0/tidy_cmd.html>.

- Pretty print an HTML file:

`tidy {{path/to/file.html}}`

- Enable identation, wrapping lines in 100, saving to `output.html`:

`tidy --indent y --wrap 100 -output {{path/to/output.html}} {{path/to/file.html}}`

- Modify an HTML file in-place using a config file:

`tidy -config {{path/to/config}} -modify {{path/to/file.html}}`
