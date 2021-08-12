# eyeD3

> Citiți și manipulați metadatele fișierelor MP3.
> Mai multe informaţii: <https://eyed3.readthedocs.io/en/latest/>

- Vizualizați informații despre un fișier MP3:

`eyeD3 {{filename.mp3}}`

- Setați titlul unui fișier MP3:

`eyeD3 --title "{{A Title}}" {{filename.mp3}}`

- Setați albumul tuturor fișierelor MP3 într-un director:

`eyeD3 --album "{{Album Name}}" {{*.mp3}}`

- Setați coperta frontală pentru un fișier MP3:

`eyeD3 --add-image {{front_cover.jpeg}}:FRONT_COVER: {{filename.mp3}}`
