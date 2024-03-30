# pamtowinicon

> Convert a PAM image to a Windows ICO file.
> More information: <https://netpbm.sourceforge.net/doc/pamtowinicon.html>.

- Convert a PAM image file to an ICO file:

`pamtowinicon {{path/to/input_file.pam}} > {{path/to/output.ico}}`

- Encode images with resolutions smaller than t in the BMP format and all other images in the PNG format:

`pamtowinicon -pngthreshold {{t}} {{path/to/input_file.pam}} > {{path/to/output.ico}}`

- Make all pixels outside the non-opaque area black:

`pamtowinicon -truetransparent {{path/to/input_file.pam}} > {{path/to/output.ico}}`
