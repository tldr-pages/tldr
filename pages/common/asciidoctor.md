# asciidoctor

> An AsciiDoc processor to read and translate AsciiDoc to a publishable format.
> More information: <https://docs.asciidoctor.org>.

- Convert `path/to/document.adoc` to HTML (the default output format):

`asciidoctor {{path/to/document.adoc}}`

- Convert `path/to/document.adoc` to HTML and link `path/to/style.css`:

`asciidoctor -a stylesheet={{path/to/style.css}} {{path/to/document.adoc}}`

- Convert `path/to/document.adoc` to embeddable HTML, removing everything except the body:

`asciidoctor --embedded {{path/to/document.adoc}}`

- Convert `path/to/document.adoc` to PDF using the `asciidoctor-pdf` library:

`asciidoctor --backend=pdf --require=asciidoctor-pdf {{path/to/document.adoc}}`
