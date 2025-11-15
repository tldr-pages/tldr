# pdfcrop

> Detect and remove margins in each page in a PDF file.
> More information: <https://github.com/ho-tex/pdfcrop>.

- Automatically detect and remove the margin for each page in a PDF file:

`pdfcrop {{path/to/input_file.pdf}} {{path/to/output_file.pdf}}`

- Set the margins of each page to a specific value:

`pdfcrop {{path/to/input_file.pdf}} --margins '{{left}} {{top}} {{right}} {{bottom}}' {{path/to/output_file.pdf}}`

- Set the margins of each page to a specific value, using the same value for left, top, right and bottom:

`pdfcrop {{path/to/input_file.pdf}} --margins {{300}} {{path/to/output_file.pdf}}`

- Use a user-defined bounding box for cropping instead of automatically detecting it:

`pdfcrop {{path/to/input_file.pdf}} --bbox '{{left}} {{top}} {{right}} {{bottom}}' {{path/to/output_file.pdf}}`

- Use different user-defined bounding boxes for odd and even pages:

`pdfcrop {{path/to/input_file.pdf}} --bbox-odd '{{left}} {{top}} {{right}} {{bottom}}' --bbox-even '{{left}} {{top}} {{right}} {{bottom}}' {{path/to/output_file.pdf}}`

- Automatically detect margins using a lower resolution for improved performance:

`pdfcrop {{path/to/input_file.pdf}} --resolution {{72}} {{path/to/output_file.pdf}}`
