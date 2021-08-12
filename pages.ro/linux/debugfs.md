# debugfs

> Un depanator interactiv al sistemului de fișiere ext2/ext3/ext4.
> Mai multe informaţii: <https://manned.org/debugfs>

- Deschideți sistemul de fișiere în modul doar citire:

`debugfs {{/dev/sdXN}}`

- Deschideți sistemul de fișiere în modul citire scriere:

`debugfs -w {{/dev/sdXN}}`

- Citiți comenzile dintr-un fișier specificat, executați-le și apoi ieșiți:

`debugfs -f {{path/to/cmd_file}} {{/dev/sdXN}}`

- Vizualizaţi statisticile sistemului de fişiere în consola debugfs:

`stats`

- Închideți sistemul de fișiere:

`close -a`

- Listează toate comenzile disponibile:

`lr`
