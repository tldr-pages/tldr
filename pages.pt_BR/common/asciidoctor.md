# asciidoctor

> Um processador que converte AsciiDoc em formatos publicáveis.
> Mais informações: <https://docs.asciidoctor.org>.

- Converte um arquivo `.adoc` em HTML (formato padrão de saída):

`asciidoctor {{caminho/para/arquivo.adoc}}`

- Converte um arquivo `.adoc` em HTML e liga a uma folha de estilos CSS:

`asciidoctor -a stylesheet={{caminho/para/estilos.css}} {{caminho/para/arquivo.adoc}}`

- Converte um arquivo `.adoc` em um HTML embutível, removendo tudo exceto o corpo:

`asciidoctor --embedded {{caminho/para/arquivo.adoc}}`

- Converte um arquivo `.adoc` em PDF usando a biblioteca `asciidoctor-pdf`:

`asciidoctor --backend={{pdf}} --require={{asciidoctor-pdf}} {{caminho/para/arquivo.adoc}}`
