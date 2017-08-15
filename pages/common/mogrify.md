# Mogrify

> Tool that allows making operations on multiple image files ie. resizing, cropping, flipping, adding effects.

- Resize all jpg images in the folder to 50% of initial size:

`mogrify -resize 50% *.jpg`

- Resize all images starting with DSC to 600x400:

`mogrify -resize 800x600 DSC*`

- Convert all png images in the folder to jpg:

`mogrify -format jpg *.png`

- Halve the saturation for all files:

`mogrify -modulate 100,50 *`

- Double the brightness:

`mogrify -modulate 200 *`
