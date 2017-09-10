# pdfposter

> Convert a large-sheeted pdf into multiple A4 tiles for printing.

- Convert an A2 poster into 4 A4 tiles:

`pdfposter --poster-size a2 {{input_file.pdf}} {{output_file.pdf}}`

- Scale an A4 poster to A3 and then generate 2 A4 tiles:

`pdfposter --scale 2 {{input_file.pdf}} {{output_file.pdf}}`
