# ipconfig

> Mostra e gestisce le configurazioni di rete di Windows.
> Maggiori informazioni: <https://learn.microsoft.com/windows-server/administration/windows-commands/ipconfig>.

- Mostra la lista delle schede di rete:

`ipconfig`

- Mostra la lista dettagliata delle schede di rete:

`ipconfig /all`

- Rinnova l'indirizzo IP di una scheda di rete:

`ipconfig /renew {{scheda_di_rete}}`

- Libera gli indirizzi IP per una scheda di rete:

`ipconfig /release {{scheda_di_rete}}`

- Rimuovi tutti i dati dalla cache DNS:

`ipconfig /flushdns`
