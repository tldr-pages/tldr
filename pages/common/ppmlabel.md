# ppmlabel

> Add text to a PPM image.
> More information: <https://netpbm.sourceforge.net/doc/ppmlabel.html>.

- Add text to a PPM image at the specified location:

`ppmlabel -x {{pos_x}} -y {{pos_y}} {{[-t|-text]}} {{text}} {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`

- Add multiple texts at different locations:

`ppmlabel -x {{pos_x1}} -y {{pos_y1}} {{[-t|-text]}} {{text1}} -x {{pos_x2}} -y {{pos_y2}} {{[-t|-text]}} {{text2}} {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`

- Specify the line color, the background color, the tilt and the size of the added text:

`ppmlabel -x {{pos_x}} -y {{pos_y}} {{[-c|-color]}} {{line_color}} {{[-b|-background]}} {{background_color}} {{[-a|-angle]}} {{tilt}} {{[-s|-size]}} {{size}} {{[-t|-text]}} {{text}} {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`
