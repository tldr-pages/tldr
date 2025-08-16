# xgettext

> Extract gettext strings from code files.
> More information: <https://www.gnu.org/software/gettext/manual/gettext.html#xgettext-Invocation>.

- Scan file and output strings to `messages.po`:

`xgettext {{path/to/input_file}}`

- Use a different output filename:

`xgettext {{[-o|--output]}} {{path/to/output_file}} {{path/to/input_file}}`

- Append new strings to an existing file:

`xgettext {{[-j|--join-existing]}} {{[-o|--output]}} {{path/to/output_file}} {{path/to/input_file}}`

- Don't add a header containing metadata to the output file:

`xgettext --omit-header {{path/to/input_file}}`

- Display help:

`xgettext {{[-h|--help]}}`
