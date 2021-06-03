# mkvmerge

> Merge and extract multimedia streams.
> More information: <https://mkvtoolnix.download/doc/mkvmerge.html>.

- Display information about a Matroska file:

`mkvmerge --identify {{path/to/file.mkv}}`

- Extract the audio from track 1 of a specific file:

`mkvextract tracks {{path/to/file.mkv}} {{1}}:{{path/to/output.webm}}`

- Extract the subtitle from track 3 of a specific file:

`mkvextract tracks {{path/to/file.mkv}} {{3}}:{{path/to/subs.srt}}`
