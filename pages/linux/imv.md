# imv

> CLI image viewer for wayland and X11 aimed to tiling window managers.
> Handles multiple formats including photoshop(PSD).
> More information: <https://sr.ht/~exec64/imv>.

- View multiple images:

`imv {{path/to/image1.ext path/to/image2.ext ...}}`

- View in fullscreen mode:

`imv -f {{path/to/image.ext}}`

- View images recursively in a directory:

`imv --slideshow {{path/to/image.ext}}`

- Open multiple images via `stdin`:

`find . -type f -name "{{*.svg}}" | imv`

- Make a slideshow from a directory showing each image for 10 seconds:

`imv -t 10 {{path/to/directory}}`

- View multiple images from the web:

`curl -Osw '%{filename_effective}\n' '{{http://www.example.com/[1-10].jpg}}' | imv`
