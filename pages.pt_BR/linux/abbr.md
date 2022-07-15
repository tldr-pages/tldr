# abbr

> Gerencie abreviaçoes para fish-shell.
> Palavras definidas pelo usuário são substituídas por frases longas assim que são digitadas.
> Mais informações: <https://fishshell.com/docs/current/cmds/abbr.html>.

- Adicione uma nova abreviação:

`abbr --add {{abbreviation_name}} {{command}} {{command_arguments}}`

- Renomear uma abreviação existente:

`abbr --rename {{old_name}} {{new_name}}`

- Apagar uma abreviação existente:

`abbr --erase {{abbreviation_name}}`

- Importar abreviações definidas em outro host via SSH:

`ssh {{host_name}} abbr --show | source`
