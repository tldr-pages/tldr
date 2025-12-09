# fsck

> Controlla l'integrità di un filesystem o lo ripara. Il filesystem non dev'essere montato al momento in cui il comando viene eseguito.
> Maggiori informazioni: <https://manned.org/fsck>.

- Controlla il filesystem `/dev/sdX`, riportando eventuali blocchi danneggiati:

`sudo fsck {{/dev/sdX}}`

- Controlla il filesystem `/dev/sdX`, riportando eventuali blocchi danneggiati e per ognuno consente all'utente di scegliere interattivamente se ripararlo:

`sudo fsck -r {{/dev/sdX}}`

- Controlla il filesystem `/dev/sdX`, riportando eventuali blocchi danneggiati e riparandoli automaticamente:

`sudo fsck -a {{/dev/sdX}}`
