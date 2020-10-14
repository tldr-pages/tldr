# tail

> Exibir a ultima parte de um arquivo.
> Mais informações: <https://linux.die.net/man/1/tail>.

- Exibir as ultimas 10 linhas do conteúdo de um arquivo:

`tail {{nome_do_arquivo}}`

- Exibir as ultimas {{numero_de_linhas}} linhas do conteúdo de um arquivo:

`tail {{nome_do_arquivo}} -n {{limite_de_linhas}}`

- Exibir o conteúdo de um arquivo e conforme novos dados são inseridos os mesmos serão mostrados:

`tail -f {{nome_do_arquivo}}`
