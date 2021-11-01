# mp3info

> Viewer/editor for ID3v1 (but not ID3v2) tags of MP3 files.
> More information: <http://www.ibiblio.org/mp3info>.

- Show all ID3v1 tags of a specific MP3 file:

`mp3info {{path/to/file.mp3}}`

- Edit ID3v1 tags interactively:

`mp3info -i {{path/to/mp3file}}`

- Set values for ID3v1 tags in a specific MP3 file:

`mp3info -a "{{artist_name}}" -t "{{song_title}}" -l "{{album_title}}" -y {{year}} -c "{{comment_text}}" {{path/to/file.mp3}}`

- Set number of track on album:

`mp3info -n {{track_number}} {{path/to/mp3file}}`

- Print list of numbers for all music genres:

`mp3info -G`

- Set music genre for MP3 file:

`mp3info -g {{genre_number}} {{path/to/file.mp3}}`
