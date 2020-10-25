# fsck

> Controlla l'integrità di un filesystem o lo ripara. Il filesystem non dev'essere montato al momento in cui il comando viene eseguito.

- Controlla il filesystem /dev/sda, riportando eventuali blocchi danneggiati:

`fsck {{/dev/sda}}`

- Controlla il filesystem /dev/sda, riportando eventuali blocchi danneggiati e per ognuno consente all'utente di scegliere interattivamente se ripararlo:

`fsck -r {{/dev/sda}}`

- Controlla il filesystem /dev/sda, riportando eventuali blocchi danneggiati e riparandoli automaticamente:

`fsck -a {{/dev/sda}}`
