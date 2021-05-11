# mkvmerge

> Merge and extract multimedia streams
> More information: <https://mkvtoolnix.download/doc/mkvmerge.html>.

- Print information about the source file:

`mkvmerge --identify {{path/to/file.mkv}}`

- Extract the audio:

`mkvextract tracks {{file.mkv}} {{1}}:{{audio.webm}}`

- Extract a subtitle track:

`mkvextract tracks {{file.mkv}} {{3}}:{{subs.srt}}`
