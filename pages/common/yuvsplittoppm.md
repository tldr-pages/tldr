# yuvsplittoppm

> Convert three subsampled Abekas YUV files to one PPM image.
> More information: <https://netpbm.sourceforge.net/doc/yuvsplittoppm.html>.

- Read Akebas YUV bytes from three files starting with basename, merge them into a single PPM image and store it in the specified output file:

`yuvsplittoppm {{basename}} {{width}} {{height}} > {{path/to/output_file.ppm}}`
