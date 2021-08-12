# pdfseparate

> Portable Document Format (PDF) pagina de extractor.
> Mai multe informaţii: <https://manpages.debian.org/unstable/poppler-utils/pdfseparate.1.en.html>

- Extrageți paginile din fișierul PDF și creați un fișier PDF separat pentru fiecare pagină:

`pdfseparate {{path/to/source_filename.pdf}} {{path/to/destination_filename-%d.pdf}}`

- Specificați prima pagină de start pentru extracție:

`pdfseparate -f {{3}} {{path/to/source_filename.pdf}} {{path/to/destination_filename-%d.pdf}}`

- Specificați ultima pagină pentru extracție:

`pdfseparate -l {{10}} {{path/to/source_filename.pdf}} {{path/to/destination_filename-%d.pdf}}`
