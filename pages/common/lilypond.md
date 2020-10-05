# lilypond

> Typeset music and/or produce MIDI from file.
> More information: <https://lilypond.org/index.html>.

- Compile a lilypond file into a PDF:

`lilypond {{path/to/file}}`

- Compile file into specified format:

`lilypond --formats={{format_dump}} {{name_file}}`

- Compile file, suppressing progress:

`lilypond -s {{name_file}}`

- Compile file into specified output name:

`lilypond --output={{name_output}} {{name_file}}`

- Show version of tool:

`lilypond --version`
