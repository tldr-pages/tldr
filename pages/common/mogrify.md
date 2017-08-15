# mogrify

> Tool that allows making operations on multiple image files
> ie. resizing, cropping, flipping, adding effects

- resize all jpg images in the folder to 50% of initial size:

`mogrify -resize 50% *.jpg`

- resize all images starting with DSC to 600x400:

`mogrify -resize 800x600 DSC*`

- convert all png images in the folder to jpg:

`mogrify -format jpg *.png`

- halve the saturation for all files:

`mogrify -modulate 100,50 *`

- double the brightness:

`mogrify -modulate 200 *`
