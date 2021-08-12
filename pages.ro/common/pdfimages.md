# pdfimages

> Utilitar pentru extragerea imaginilor din PDF-uri.

- Extrageţi toate imaginile dintr-un fişier PDF şi salvaţi-le ca PNG-uri:

`pdfimages -png {{path/to/file.pdf}} {{filename_prefix}}`

- Extragerea imaginilor de la paginile 3 la 5:

`pdfimages -f {{3}} -l {{5}} {{path/to/file.pdf}} {{filename_prefix}}`

- Extrageţi imagini dintr-un fişier PDF şi includeţi numărul paginii în numele fişierelor de ieşire:

`pdfimages -p {{path/to/file.pdf}} {{filename_prefix}}`

- Listați informații despre toate imaginile dintr-un fișier PDF:

`pdfimages -list {{path/to/file.pdf}}`
