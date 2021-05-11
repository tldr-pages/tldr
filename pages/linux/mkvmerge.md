# mkvmerge

> Merge and extract multimedia streams
> More information: <https://github.com/topics/mkvmerge>.

- Print information about the source file:

`mkvmerge --identify {{file.mkv}}`

- Extract the audio:

`mkvextract tracks {{file.mkv}} {{1}}:{{audio.webm}}`

- Extract a subtitle track:

`mkvextract tracks {{file.mkv}} {{3}}:{{subs.srt}}`
