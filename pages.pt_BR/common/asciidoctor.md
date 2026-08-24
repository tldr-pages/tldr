# asciidoctor

> Um processador que converte AsciiDoc em formatos publicáveis.
> Mais informações: <https://docs.asciidoctor.org/asciidoctor/latest/cli/man1/asciidoctor/>.

- Converte um arquivo `.adoc` em HTML (formato padrão de saída):

`asciidoctor {{caminho/para/arquivo.adoc}}`

- Converte um arquivo `.adoc` em HTML e liga a uma folha de estilos CSS:

`asciidoctor {{[-a|--attribute]}} stylesheet={{caminho/para/estilos.css}} {{caminho/para/arquivo.adoc}}`

- Converte um arquivo `.adoc` em um HTML embutível, removendo tudo exceto o corpo:

`asciidoctor {{[-e|--embedded]}} {{caminho/para/arquivo.adoc}}`

- Converte um arquivo `.adoc` em PDF usando a biblioteca `asciidoctor-pdf`:

`asciidoctor {{[-b|--backend]}} pdf {{[-r|--require]}} asciidoctor-pdf {{caminho/para/arquivo.adoc}}`
