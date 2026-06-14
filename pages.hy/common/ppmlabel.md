# ppm պիտակ

> Ավելացնել տեքստ PPM պատկերին:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/ppmlabel.html>:.

- Տեքստ ավելացրեք PPM պատկերին նշված վայրում.:

`ppmlabel -x {{pos_x}} -y {{pos_y}} {{[-t|-text]}} {{text}} {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`

- Ավելացրեք բազմաթիվ տեքստեր տարբեր վայրերում.:

`ppmlabel -x {{pos_x1}} -y {{pos_y1}} {{[-t|-text]}} {{text1}} -x {{pos_x2}} -y {{pos_y2}} {{[-t|-text]}} {{text2}} {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`

- Նշեք տողի գույնը, ֆոնի գույնը, թեքությունը և ավելացված տեքստի չափը.:

`ppmlabel -x {{pos_x}} -y {{pos_y}} {{[-c|-color]}} {{line_color}} {{[-b|-background]}} {{background_color}} {{[-a|-angle]}} {{tilt}} {{[-s|-size]}} {{size}} {{[-t|-text]}} {{text}} {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`
