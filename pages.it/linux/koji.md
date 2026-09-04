# koji

> Interagisce con kojihub.
> Alcuni sottocomandi come `build`, `tag-build`, `download-build`, `buildinfo`, `call`, ecc. hanno la propria documentazione d'uso.
> Maggiori informazioni: <https://docs.pagure.org/koji/>.

- Esegue un sottocomando koji:

`koji {{sottocomando}}`

- Si presenta per testare la connettività con kojihub:

`koji moshimoshi`

- Mostra aiuto sulle opzioni globali:

`koji {{[-h|--help]}}`

- Mostra aiuto per ottenere tutti i comandi disponibili:

`koji help`

- Mostra aiuto per un sottocomando specifico (come `build`, `tag-build`, `download-build`, `buildinfo`, `call`, ecc.):

`koji {{sottocomando}} {{[-h|--help]}}`

- Mostra versione:

`koji version`
