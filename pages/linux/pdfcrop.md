# pdfcrop

> Detect and remove margins in each page in a PDF file.
> More information: <https://github.com/ho-tex/pdfcrop>.

- Automatically detect and remove margin for each page in a PDF file:

`pdfcrop {{path/to/file.pdf}} {{path/to/out_file.pdf}}`

- Set the margins of each page to a specific value:

`pdfcrop {{path/to/file.pdf}} --margins '{{300 180 400 150}}' {{path/to/out_file.pdf}}`

- Set the margins of each page to a specific value, using the same value for left, top, right and bottom:

`pdfcrop {{path/to/file.pdf}} --margins {{300}} {{path/to/out_file.pdf}}`

- Use a user-defined bounding box for cropping instead of automatically detecting it:

`pdfcrop {{path/to/file.pdf}} --bbox '{{150 200 180 220}}' {{path/to/out_file.pdf}}`

- Use different user-defined bounding boxes for odd and even pages:

`pdfcrop {{path/to/file.pdf}} --bbox-odd '{{150 200 180 220}}' --bbox-even '{{180 200 150 220}}' {{path/to/out_file.pdf}}`

- Automatically detect margins using a lower resolution for improved performance:

`pdfcrop {{path/to/file.pdf}} --resolution {{72}} {{path/to/out_file.pdf}}`
