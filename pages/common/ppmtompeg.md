# ppmtompeg

> Encode an MPEG-1 stream.
> More information: <https://netpbm.sourceforge.net/doc/ppmtompeg.html>.

- Produce an MPEG-1 stream using the parameter file to specify inputs and outputs:

`ppmtompeg {{path/to/parameter_file}}`

- Encode the GOP with the specified number only:

`ppmtompeg -gop {{gop_num}} {{path/to/parameter_file}}`

- Specify the first and last frame to encode:

`ppmtompeg -frames {{first_frame}} {{last_frame}} {{path/to/parameter_file}}`

- Combine multiple MPEG frames into a single MPEG-1 stream:

`ppmtompeg -combine_frames {{path/to/parameter_file}}`
