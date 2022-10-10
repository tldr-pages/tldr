# ebook-convert

> Pode ser usado para converter e-books entre os fomatos comuns, como PDF, EPUB e MOBI.
> Faz parte da biblioteca de ferramentas Calibre e-book.
> Mais informações: <https://manual.calibre-ebook.com/generated/en/ebook-convert.html>.

- Converter um e-book em outro formato:

`ebook-convert {{original}} {{formato_pretendido}}`

- Converter Markdown ou HTML em um e-book com ToC, título e autor:

`ebook-convert {{original}} {{formato_pretendido}} --level1-toc="//h:h1" --level2-toc="//h:h2" --level3-toc="//h:h3" --title={{titulo}} --authors={{autor}}`
