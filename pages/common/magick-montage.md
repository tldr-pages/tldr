# magick montage

> Tile images into a customizable grid.
> See also: `magick`.
> More information: <https://imagemagick.org/script/montage.php>.

- Tile images into a grid, automatically resizing images larger than the grid cell size:

`magick montage {{path/to/image1.jpg path/to/image2.jpg ...}} {{path/to/montage.jpg}}`

- Tile images into a grid, automatically calculating the grid cell size from the largest image:

`magick montage {{path/to/image1.jpg path/to/image2.jpg ...}} -geometry {{+0+0}} {{path/to/montage.jpg}}`

- Specify the grid cell size and resize images to fit it before tiling:

`magick montage {{path/to/image1.jpg path/to/image2.jpg ...}} -geometry {{640x480+0+0}} {{path/to/montage.jpg}}`

- Limit the number of rows and columns in the grid, causing input images to overflow into multiple output montages:

`magick montage {{path/to/image1.jpg path/to/image2.jpg ...}} -geometry {{+0+0}} -tile {{2x3}} {{montage_%d.jpg}}`

- Resize and crop images to fill their grid cells before tiling:

`magick montage {{path/to/image1.jpg path/to/image2.jpg ...}} -geometry {{+0+0}} -resize {{640x480^}} -gravity {{center}} -crop {{640x480+0+0}} {{path/to/montage.jpg}}`
