# ppmlabel

> Add text to a PPM image.
> More information: <https://netpbm.sourceforge.net/doc/ppmlabel.html>.

- Add text to a PPM image at the specified location:

`ppmlabel -x {{pos_x}} -y {{pos_y}} -text {{text}} {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`

- Add multiple texts at different locations:

`ppmlabel -x {{pos_x1}} -y {{pos_y1}} -text {{text1}} -x {{pos_x2}} -y {{pos_y2}} -text {{text2}} {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`

- Specify the line color, the background color, the tilt and the size of the added text:

`ppmlabel -x {{pos_x}} -y {{pos_y}} -color {{line_color}} -background {{background_color}} -angle {{tilt}} -size {{size}} -text {{text}} {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`
