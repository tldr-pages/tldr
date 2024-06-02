# pcdovtoppm

> Create an index image for a photo CD based on its overview file.
> More information: <https://netpbm.sourceforge.net/doc/pcdovtoppm.html>.

- Create a PPM index image from a PCD overview file:

`pcdovtoppm {{path/to/file.pcd}} > {{path/to/output.ppm}}`

- Specify the [m]aximum width of the output image and the maximum [s]ize of each of the images contained in the output:

`pcdovtoppm -m {{width}} -s {{size}} {{path/to/file.pcd}} > {{path/to/output.ppm}}`

- Specify the maximum number of images [a]cross and the maximum number of [c]olours:

`pcdovtoppm -a {{n_images}} -c {{n_colours}} {{path/to/file.pcd}} > {{path/to/output.ppm}}`

- Use the specified [f]ont for annotations and paint the background [w]hite:

`pcdovtoppm -f {{font}} -w {{path/to/file.pcd}} > {{path/to/output.ppm}}`
