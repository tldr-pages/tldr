# magick mogrify

> Perform operations on multiple images, such as resizing, cropping, flipping, and adding effects.
> Changes are applied directly to the original file.
> See also: `magick`.
> More information: <https://imagemagick.org/script/mogrify.php>.

- Resize all JPEG images in the directory to 50% of their initial size:

`magick mogrify -resize {{50%}} {{*.jpg}}`

- Resize all images starting with `DSC` to 800x600:

`magick mogrify -resize {{800x600}} {{DSC*}}`

- Convert all PNGs in the directory to JPEG:

`magick mogrify -format {{jpg}} {{*.png}}`

- Halve the saturation of all image files in the current directory:

`magick mogrify -modulate {{100,50}} {{*}}`

- Double the brightness of all image files in the current directory:

`magick mogrify -modulate {{200}} {{*}}`
