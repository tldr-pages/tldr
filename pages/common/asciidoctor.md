# asciidoctor

> Convert AsciiDoc files to a publishable format.
> More information: <https://docs.asciidoctor.org/asciidoctor/latest/cli/man1/asciidoctor/>.

- Convert a specific `.adoc` file to HTML (the default output format):

`asciidoctor {{path/to/file.adoc}}`

- Convert a specific `.adoc` file to HTML and link a CSS stylesheet:

`asciidoctor {{[-a|--attribute]}} stylesheet={{path/to/stylesheet.css}} {{path/to/file.adoc}}`

- Convert a specific `.adoc` file to embeddable HTML, removing everything except the body:

`asciidoctor {{[-e|--embedded]}} {{path/to/file.adoc}}`

- Convert a specific `.adoc` file to a PDF using the `asciidoctor-pdf` library:

`asciidoctor {{[-b|--backend]}} pdf {{[-r|--require]}} asciidoctor-pdf {{path/to/file.adoc}}`
