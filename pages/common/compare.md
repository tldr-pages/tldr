# compare

> Create a comparison image to visually annotate the difference between two images.
> Part of ImageMagick.
> More information: <https://imagemagick.org/script/compare.php>.

- Compare two images:

`compare {{path/to/image1.png}} {{path/to/image2.png}} {{path/to/diff.png}}`

- Compare two images using the specified metric:

`compare -verbose -metric {{PSNR}} {{path/to/image1.png}} {{path/to/image2.png}} {{path/to/diff.png}}`
