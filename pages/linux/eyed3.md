# eyeD3

> Read and manipulate metadata of MP3 files.
> More information: <https://eyed3.readthedocs.io>.

- View information about an MP3 file:

`eyeD3 {{filename.mp3}}`

- Set the title of an MP3 file:

`eyeD3 --title "{{A Title}}" {{filename.mp3}}`

- Set the album of all the MP3 files in a directory:

`eyeD3 --album "{{Album Name}}" {{*.mp3}}`

- Set the front cover art for an MP3 file:

`eyeD3 --add-image {{front_cover.jpeg}}:FRONT_COVER: {{filename.mp3}}`
