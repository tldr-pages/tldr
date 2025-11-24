# lilypond

> Typeset music and/or produce MIDI from file.
> See also: `musescore`.
> More information: <https://lilypond.org/doc/v2.24/Documentation/usage/command_002dline-usage>.

- Compile a lilypond file into a PDF:

`lilypond {{path/to/file}}`

- Compile into the specified format:

`lilypond {{[-f|--format]}} {{format_dump}} {{path/to/file}}`

- Compile the specified file, suppressing progress updates:

`lilypond {{[-s|--silent]}} {{path/to/file}}`

- Compile the specified file, and also specify the output filename:

`lilypond {{[-o|--output]}} {{path/to/output_file}} {{path/to/input_file}}`

- Display version:

`lilypond {{[-v|--version]}}`
