# feh

> Lightweight image viewing utility.

- View images locally or using a URL:

`feh {{path/to/images}}`

- View images recursively:

`feh --recursive {{path/to/images}}`

- View images without window borders:

`feh --borderless {{path/to/images}}`

- Exit after the last image:

`feh --cycle-once {{path/to/images}}`

- Set the slideshow cycle delay:

`feh --slideshow-delay {{seconds}} {{path/to/images}}`

- Set your wallpaper (centered, filled, maximized, scaled or tiled):

`feh --bg-{{center|fill|max|scale|tile}} {{path/to/image}}`

- Create a montage of all images within a directory. Outputs as a new image:

`feh --montage --thumb-height {{150}} --thumb-width {{150}} --index-info "{{%nn%wx%h}}" --output {{path/to/montage_image.png}}`
