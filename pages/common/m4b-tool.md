# m4b-tool

> Merge, split, and manipulate audiobook files with chapters.
> More information: <https://github.com/sandreas/m4b-tool>.

- Create an audiobook with the audio files in the input directory:

`m4b-tool merge {{path/to/input_directory}} {{[-o|--output-file]}}={{path/to/merged.m4b}}`

- Make chapters using the input files' names:

`m4b-tool merge {{path/to/input_directory}} {{[-o|--output-file]}}={{path/to/merged.m4b}} --use-filenames-as-chapters`

- Split an audiobook into separate files by chapters:

`m4b-tool split {{path/to/audiobook.m4b}} {{[-o|--output-dir]}}={{path/to/output_directory}}`

- Split an audiobook into MP3 files:

`m4b-tool split {{path/to/audiobook.m4b}} --audio-format {{mp3}} {{[-o|--output-dir]}}={{path/to/output_directory}}`

- Adjust chapters using silence detection:

`m4b-tool chapters {{path/to/audiobook.m4b}} --adjust-by-silence`
