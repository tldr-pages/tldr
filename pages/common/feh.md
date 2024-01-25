# feh

> Lightweight image viewing utility.
> More information: <https://feh.finalrewind.org>.

- View images locally or using a URL:

`feh {{path/to/images}}`

- View images recursively:

`feh --recursive {{path/to/images}}`

- View images without window borders:

`feh --borderless {{path/to/images}}`

- Exit after the last image:

`feh --cycle-once {{path/to/images}}`

- Use a specific slideshow cycle delay:

`feh --slideshow-delay {{seconds}} {{path/to/images}}`

- Use a specific wallpaper mode (centered, filled, maximized, scaled or tiled):

`feh --bg-{{center|fill|max|scale|tile}} {{path/to/image}}`

- Create a montage of all images within a directory, outputting as a new image:

`feh --montage --thumb-height {{150}} --thumb-width {{150}} --index-info "{{%nn%wx%h}}" --output {{path/to/montage_image.png}}`
