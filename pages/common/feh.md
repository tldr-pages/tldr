# feh

> Lightweight image viewing utility.
> More information: <https://man.finalrewind.org/1/feh/>.

- View images locally or using a URL:

`feh {{path/to/images}}`

- View images recursively:

`feh {{[-r|--recursive]}} {{path/to/images}}`

- View images and display the file name at the top-left of the images:

`feh {{[-d|--draw-filename]}} {{path/to/images}}`

- View images without window borders:

`feh {{[-x|--borderless]}} {{path/to/images}}`

- Set the behavior when reaching the beginning or end of the image list:

`feh --on-last-slide {{hold|quit|resume}} {{path/to/images}}`

- Use a specific slideshow cycle delay:

`feh {{[-D|--slideshow-delay]}} {{seconds}} {{path/to/images}}`

- Use a specific wallpaper mode (centered, filled, maximized, scaled or tiled):

`feh --bg-{{center|fill|max|scale|tile}} {{path/to/image}}`

- Create a montage of all images within a directory, outputting as a new image:

`feh {{[-m|--montage]}} {{[-E|--thumb-height]}} {{150}} {{[-y|--thumb-width]}} {{150}} --index-info "{{%nn%wx%h}}" {{[-o|--output]}} {{path/to/montage_image.png}}`
