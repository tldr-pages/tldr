# eyeD3

> MP3 fájlok metaadatainak olvasása és kezelése. További információ: <https://eyed3.readthedocs.io>.

- MP3-fájlra vonatkozó információk megtekintése:

`eyeD3 {{filename.mp3}}`

- Az MP3-fájl címének beállítása:

`eyeD3 --title "{{A Title}}" {{filename.mp3}}`

- Egy könyvtárban található összes MP3-fájl albumának beállítása:

`eyeD3 --album "{{Album Name}}" {{*.mp3}}`

- Egy MP3-fájl borítójának beállítása:

`eyeD3 --add-image {{front_cover.jpeg}}:FRONT_COVER: {{filename.mp3}}`
