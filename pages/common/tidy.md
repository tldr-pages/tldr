# tidy

> Clean up and pretty print HTML, XHTML and XML files.
> Note: `tidy` cannot preserve original indentation.
> More information: <https://api.html-tidy.org/tidy/tidylib_api_5.2.0/tidy_cmd.html>.

- Pretty print an HTML file:

`tidy {{path/to/file.html}}`

- Enable [i]ndentation, [w]rapping lines in 100, saving to `output.html`:

`tidy --indent y --wrap 100 -output {{path/to/output.html}} {{path/to/file.html}}`

- Modify an HTML file in-place using a configuration file:

`tidy -config {{path/to/configuration}} -modify {{path/to/file.html}}`
