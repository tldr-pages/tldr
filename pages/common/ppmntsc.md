# ppmntsc

> Make the RGB colors in a PPM image compatible with NTSC or PAL color systems.
> More information: <https://netpbm.sourceforge.net/doc/ppmntsc.html>.

- Make the RGB colors in a PPM image compatible with NTSC color systems:

`ppmntsc {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`

- Make the RGB colors in a PPM image compatible with PAL color systems:

`ppmntsc --pal {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`

- Print the number of illegal pixels in the input image to `stderr`:

`ppmntsc --verbose {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`

- Output only legal/illegal/corrected pixels, set other pixels to black:

`ppmntsc --{{legalonly|illegalonly|correctedonly}} {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`
