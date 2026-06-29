# kid3-cli

> Command-line tagger for audio files such as MP3, M4A, FLAC, and Ogg.
> Commands are passed with `-c` and run on the file paths that follow.
> More information: <https://kid3.kde.org/>.

- Display all tag frames of one or more files:

`kid3-cli -c get {{path/to/file1.mp3 path/to/file2.mp3 ...}}`

- Get a specific tag frame (e.g. `artist`, `album`, `title`):

`kid3-cli -c "get {{artist}}" {{path/to/file.mp3}}`

- Set a tag frame to a value and save:

`kid3-cli -c "set {{title}} {{My Song}}" -c save {{path/to/file.mp3}}`

- Generate tags from the filename using a format string:

`kid3-cli -c "totag '{{%{artist} - %{title}}}'" -c save {{path/to/file.mp3}}`

- Generate the filename from tags using a format string:

`kid3-cli -c "fromtag '{{%{track} - %{title}}}'" -c save {{path/to/file.mp3}}`

- Convert ID3v2.3 tags to ID3v2.4 and save:

`kid3-cli -c to24 -c save {{path/to/file.mp3}}`

- Copy frames from tag 1 (ID3v1) to tag 2 (ID3v2) and save:

`kid3-cli -c "syncto {{2}}" -c save {{path/to/file.mp3}}`

- Number tracks starting at a given number and save:

`kid3-cli -c "numbertracks {{1}}" -c save {{path/to/*.mp3}}`
