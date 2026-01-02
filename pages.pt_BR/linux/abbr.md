# abbr

> Gerencie abreviações para fish-shell.
> Palavras definidas pelo usuário são substituídas por frases longas assim que são digitadas.
> Mais informações: <https://fishshell.com/docs/current/cmds/abbr.html>.

- Adicione uma nova abreviação:

`abbr {{[-a|--add]}} {{nome_abreviacao}} {{comando}} {{orgumentos_comando}}`

- Renomeia uma abreviação existente:

`abbr --rename {{nome_antigo}} {{novo_nome}}`

- Apaga uma abreviação existente:

`abbr {{[-e|--erase]}} {{nome_abreviacao}}`

- Importa abreviações definidas em outro host via SSH:

`ssh {{nome_host}} abbr {{[-s|--show]}} | source`
