# nano

> Editor de texto de linha de comando. Um clone melhorado de `Pico`.
> Mais informações: <https://nano-editor.org>.

- Inicia o editor:

`nano`

- Inicia o editor sem usar arquivos de configuração:

`nano --ignorercfiles`

- Abre arquivos específicos, passando para o próximo arquivos ao fechar o anterior:

`nano {{caminho/para/arquivo1 caminho/para/arquivo2 ...}}`

- Abre um arquivo e posiciona o cursor na linha e coluna especificadas:

`nano +{{linha}},{{coluna}} {{caminho/para/arquivo}}`

- Abre um arquivo e habilita soft wrapping:

`nano --softwrap {{caminho/para/arquivo}}`

- Abre um arquivo e indenta novas linhas de acordo com a indentação da linha anterior:

`nano --autoindent {{caminho/para/arquivo}}`

- Abre um arquivo e cria um arquivo de backup (`caminho/para/arquivo~`) ao salvá-lo:

`nano --backup {{caminho/para/arquivo}}`
