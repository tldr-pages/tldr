# eyeD3

> Read and manipulate metadata of mp3 files.

- View information about an mp3 file:

`eyeD3 {{filename.mp3}}`

- Set the album of all the mp3 files in a directory:

`eyeD3 --album {{"Album Name"}} {{*.mp3}}`

- Set the front cover art for an mp3 file:

`eyeD3 --add-image {{front_cover.jpeg}}:FRONT_COVER: {{filename.mp3}}`

- Set the title of an mp3 file:

`eyeD3 --title {{"A Title"}} {{filename.mp3}}`
