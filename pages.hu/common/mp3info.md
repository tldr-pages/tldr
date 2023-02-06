# mp3info

> MP3-fájlok ID3v1 (de nem ID3v2) címkéinek megjelenítője/szerkesztője. További információ: <http://www.ibiblio.org/mp3info>.

- Egy adott MP3-fájl összes ID3v1 címkéjének megjelenítése:

`mp3info {{path/to/file.mp3}}`

- ID3v1 címkék interaktív szerkesztése:

`mp3info -i {{path/to/file.mp3}}`

- Egy adott MP3-fájl ID3v1-címkéinek értékeinek beállítása:

`mp3info -a "{{artist_name}}" -t "{{song_title}}" -l "{{album_title}}" -y {{year}} -c "{{comment_text}}" {{path/to/file.mp3}}`

- Egy adott MP3-fájl albumban található számának beállítása:

`mp3info -n {{track_number}} {{path/to/file.mp3}}`

- Az érvényes műfajok és numerikus kódjaik listájának kinyomtatása:

`mp3info -G`

- Zenei műfaj beállítása egy adott MP3-fájlhoz:

`mp3info -g {{genre_number}} {{path/to/file.mp3}}`
