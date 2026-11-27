# dnf changelog

> Visualizza i changelog per un dato pacchetto.
> Non predefinito in `dnf` ma supportato tramite `dnf-plugins-core`.
> Maggiori informazioni: <https://dnf-plugins-core.readthedocs.io/en/latest/changelog.html>.

- Visualizza tutti i changelog per un dato pacchetto:

`dnf changelog {{pacchetto}}`

- Visualizza tutti i changelog per un dato pacchetto dopo una data specificata:

`dnf changelog --since {{date}} {{pacchetto}}`

- Visualizza gli ultimi `n` changelog per un dato pacchetto:

`dnf changelog --count {{number}} {{pacchetto}}`

- Mostra solo i nuovi elementi per i pacchetti aggiornabili:

`dnf changelog --upgrades {{pacchetto}}`

- Mostra l'aiuto:

`dnf changelog --help-cmd`
