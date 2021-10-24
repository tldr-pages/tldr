# pdfposter

> Convert a large-sheeted PDF into multiple A4 pages for printing.
> More information: <https://pdfposter.readthedocs.io>.

- Convert an A2 poster into 4 A4 pages:

`pdfposter --poster-size a2 {{input_file.pdf}} {{output_file.pdf}}`

- Scale an A4 poster to A3 and then generate 2 A4 pages:

`pdfposter --scale 2 {{input_file.pdf}} {{output_file.pdf}}`
