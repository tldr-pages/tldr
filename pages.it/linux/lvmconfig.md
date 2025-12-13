# lvmconfig

> Visualizza e gestisce le informazioni di configurazione di LVM.
> Maggiori informazioni: <https://manned.org/lvmconfig>.

- Mostra la configurazione effettiva in uso (dopo aver unito tutte le sorgenti di configurazione):

`lvmconfig --typeconfig current --mergedconfig`

- Mostra solo le impostazioni che differiscono dai valori predefiniti:

`lvmconfig --typeconfig diff`

- Elenca tutte le chiavi di configurazione:

`lvmconfig {{[-l|--list]}}`

- Stampa la configurazione predefinita con commenti completi e spaziatura aggiuntiva:

`lvmconfig --typeconfig default --withcomments --withspaces`

- Convalida la configurazione completa unita e segnala gli errori:

`lvmconfig --mergedconfig --validate`

- Scrivi la configurazione effettiva corrente in un file:

`lvmconfig --typeconfig current {{[-f|--file]}} {{path/to/output.conf}}`
