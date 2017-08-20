# mogrify

> Tool that allows making operations on multiple images ie. resizing, cropping, flipping, adding effects. Replaces the original file.

- Resize all jpg images in the folder to 50% of their initial size:

`mogrify -resize {{50%}} {{*.jpg}}`

- Resize all images starting with DSC to 800x600:

`mogrify -resize {{800x600}} {{DSC*}}`

- Convert all png images in the folder to jpg:

`mogrify -format {{jpg}} {{*.png}}`

- Halve the saturation for all image files in the folder:

`mogrify -modulate {{100,50}} {{*}}`

- Double the brightness for all image files in the folder:

`mogrify -modulate {{200}} {{*}}`
