# lilypond

> Typeset music and/or produce MIDI from file.
> More information: <https://lilypond.org/index.html>.

- Compile a lilypond file into a PDF:

`lilypond {{path/to/file}}`

- Compile into the specified format:

`lilypond --formats={{format_dump}} {{path/to/file}}`

- Compile the specified file, suppressing progress updates:

`lilypond -s {{path/to/file}}`

- Compile the specified file, and also specify the output filename:

`lilypond --output={{path/to/output_file}} {{path/to/input_file}}`

- Show the current version of lilypond:

`lilypond --version`
