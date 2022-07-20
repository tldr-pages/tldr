# abbr

> Gerencie abreviações para fish-shell.
> Palavras definidas pelo usuário são substituídas por frases longas assim que são digitadas.
> Mais informações: <https://fishshell.com/docs/current/cmds/abbr.html>.

- Adicione uma nova abreviação:

`abbr --add {{nome_abreviacao}} {{comando}} {{orgumentos_comando}}`

- Renomear uma abreviação existente:

`abbr --rename {{nome_antigo}} {{novo_nome}}`

- Apagar uma abreviação existente:

`abbr --erase {{nome_abreviacao}}`

- Importar abreviações definidas em outro host via SSH:

`ssh {{nome_host}} abbr --show | source`
