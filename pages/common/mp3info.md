# mp3info

> Viewer/editor for ID3v1 (but not ID3v2) tags of MP3 files.
> More information: <https://www.ibiblio.org/mp3info/mp3info.html>.

- Show all ID3v1 tags of a specific MP3 file:

`mp3info {{path/to/file.mp3}}`

- Edit ID3v1 tags [i]nteractively:

`mp3info -i {{path/to/file.mp3}}`

- Set values for ID3v1 tags in a specific MP3 file ([a]rtist, [t]itle, a[l]bum, [y]ear, and [c]omment):

`mp3info -a "{{artist_name}}" -t "{{song_title}}" -l "{{album_title}}" -y {{year}} -c "{{comment_text}}" {{path/to/file.mp3}}`

- Set the [n]umber of the track in the album for a specific MP3 file:

`mp3info -n {{track_number}} {{path/to/file.mp3}}`

- [G]et a list of valid genres and their numeric codes:

`mp3info -G`

- Set the music [g]enre for a specific MP3 file:

`mp3info -g {{genre_number}} {{path/to/file.mp3}}`
