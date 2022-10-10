# ebook-convert

> Pode ser usado para converter e-books entre os fomatos comuns, como PDF, EPUB e MOBI.
> Faz parte da biblioteca de ferramentas Calibre e-book.
> Mais informações: <https://manual.calibre-ebook.com/generated/en/ebook-convert.html>.

- Converte um e-book em outro formato:

`ebook-convert {{caminho/para/arquivo_entrada}} {{arquivo_saída}}`

- Converte Markdown ou HTML em um e-book com ToC, título e autor:

`ebook-convert {{caminho/para/arquivo_entrada}} {{arquivo_saída}} --level1-toc="//h:h1" --level2-toc="//h:h2" --level3-toc="//h:h3" --title={{titulo}} --authors={{autor}}`
