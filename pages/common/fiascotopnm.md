# fiascotopnm

> Convert a compressed FIASCO file to a PNM image.
> More information: <https://netpbm.sourceforge.net/doc/fiascotopnm.html>.

- Convert a compressed FIASCO file to a PNM file or in the case of video streams multiple PNM files:

`fiascotopnm {{path/to/file.fiasco}} -o {{output_file_basename}}`

- Use fast decompression, resulting in a slightly decreased quality of the output file(s):

`fiascotopnm --fast {{path/to/file.fiasco}} -o {{output_file_basename}}`

- Load the options to be used from the specified configuration file:

`fiascotopnm --config {{path/to/fiascorc}} {{path/to/file.fiasco}} -o {{output_file_basename}}`

- Magnify the decompressed image(s) by a factor of 2^n:

`fiascotopnm --magnify {{n}} {{path/to/file.fiasco}} -o {{output_file_basename}}`

- Smooth the decompressed image by the specified amount:

`fiascotopnm --smooth {{n}} {{path/to/file.fiasco}} -o {{output_file_basename}}`
