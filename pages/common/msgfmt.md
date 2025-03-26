# msgfmt

> Compile message catalog to binary format.
> More information: <https://www.gnu.org/software/gettext/manual/html_node/msgfmt-Invocation.html>.

- Compile a file to `messages.mo`:

`msgfmt {{file.po}}`

- Convert a `.po` file to a `.mo` file:

`msgfmt {{path/to/file.po}} {{[-o|--output-file]}} {{path/to/file.mo}}`

- Display help:

`msgfmt {{[-h|--help]}}`
