# nano

> Editor de texto de linha de comando simples e fácil de usar. Um clone melhorado e gratuito de Pico.
> Mais informações: <https://nano-editor.org>.

- Abre um novo arquivo no nano:

`nano`

- Abre um arquivo específico:

`nano {{caminho/para/arquivo}}`

- Abre um arquivo específico, posicionando o cursor na linha e coluna especificadas:

`nano +{{linha}},{{coluna}} {{caminho/para/arquivo}}`

- Abre um arquivo específico e habilita soft wrapping:

`nano --softwrap {{caminho/para/arquivo}}`

- Abre um arquivo específico e indenta novas linhas para a indentação das linhas anteriores:

`nano --autoindent {{caminho/para/arquivo}}`

- Abre nano e cria um arquivo backup (`file~`) quando salva edições:

`nano --backup {{caminho/para/arquivo}}`
