# montage

> Tiles images into a customizable grid.
> Part of ImageMagick.
> More information: <https://imagemagick.org/script/montage.php>.

- Tile images into a grid, automatically resizing images larger than the grid cell size:

`montage {{path/to/image1.jpg path/to/image2.jpg ...}} {{path/to/montage.jpg}}`

- Tile images into a grid, automatically calculating the grid cell size from the largest image:

`montage {{path/to/image1.jpg path/to/image2.jpg ...}} -geometry {{+0+0}} {{path/to/montage.jpg}}`

- Set the grid cell size and resize images to fit it before tiling:

`montage {{path/to/image1.jpg path/to/image2.jpg ...}} -geometry {{640x480+0+0}} {{path/to/montage.jpg}}`

- Limit the number of rows and columns in the grid, causing input images to overflow into multiple output montages:

`montage {{path/to/image1.jpg path/to/image2.jpg ...}} -geometry {{+0+0}} -tile {{2x3}} {{montage_%d.jpg}}`

- Resize and crop images to fill their grid cells before tiling:

`montage {{path/to/image1.jpg path/to/image2.jpg ...}} -geometry {{+0+0}} -resize {{640x480^}} -gravity {{center}} -crop {{640x480+0+0}} {{path/to/montage.jpg}}`
