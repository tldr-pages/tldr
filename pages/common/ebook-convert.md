# ebook-convert

> Can be used to convert eBooks between common formats, e.g., pdf, epub and mobi.
> Part of the Calibre eBook library tool.
> More information: <https://manual.calibre-ebook.com/generated/en/ebook-convert.html>.

- Convert an eBook into another format:

`ebook-convert {{source}} {{destination}}`

- Convert Markdown or HTML to eBook with TOC, title and author:

`ebook-convert {{source}} {{destination}} --level1-toc="//h:h1" --level2-toc="//h:h2" --level3-toc="//h:h3" --title={{title}} --authors={{author}}`
