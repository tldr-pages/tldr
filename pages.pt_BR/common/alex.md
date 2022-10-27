# alex

> Uma ferramenta que captura escrita insensível e sem consideraçāo.
> Ajuda a encontrar no texto, frases favorecedoras de gênero, polarizantes, relacionadas à raça, insensíveis à religiao e outras frases desiguais.
> Mais informações: <https://github.com/get-alex/alex>.

- Analisa o texto do stdin:

`echo {{A rede dele parece boa}} | alex --stdin`

- Analisa todos arquivos no diretório atual:

`alex`

- Analisa um arquivo específico:

`alex {{archivo_do_texto.md}}`

- Analisa todos arquivos em Markdown exceto `example.md`:

`alex *.md !{{example.md}}`
