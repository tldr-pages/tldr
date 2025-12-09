# ebook-convert

> Can be used to convert e-books between common formats, e.g. PDF, EPUB and MOBI.
> Part of the Calibre e-book library tool.
> More information: <https://manual.calibre-ebook.com/generated/en/ebook-convert.html>.

- Convert an e-book into another format:

`ebook-convert {{path/to/input_file}} {{output_file}}`

- Convert Markdown or HTML to e-book with TOC, title and author:

`ebook-convert {{path/to/input_file}} {{output_file}} --level1-toc="//h:h1" --level2-toc="//h:h2" --level3-toc="//h:h3" --title={{title}} --authors={{author}}`
