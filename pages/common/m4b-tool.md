# m4b-tool

> A tool merge, split or and manipulate audiobook files with chapters.
> More information: <https://github.com/sandreas/m4b-tool>.

- Create an audiobook with the audio files in inputted directory:

`m4b-tool merge "data/my-audio-book/" --output-file="data/merged.m4b"`

- You can make chapters use file names by adding the flag --use-filenames-as-chapters:

`m4b-tool merge "data/my-audio-book/" --output-file="data/merged.m4b" --use-filenames-as-chapters`
