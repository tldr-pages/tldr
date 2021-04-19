# pdfseparate

> Portable Document Format (PDF) file page extractor.
> More information: <https://manned.org/pdfseparate>.

- Extract pages from PDF file and make a separate PDF file for each page:

`pdfseparate {{path/to/source_filename.pdf}} {{path/to/destination_filename-%d.pdf}}`

- Specify the first/start page for extraction:

`pdfseparate -f {{3}} {{path/to/source_filename.pdf}} {{path/to/destination_filename-%d.pdf}}`

- Specify the last page for extraction:

`pdfseparate -l {{10}} {{path/to/source_filename.pdf}} {{path/to/destination_filename-%d.pdf}}`
