# dnf changelog

> Visualizza i changelog per un dato pacchetto.
> Non predefinito in `dnf` ma supportato tramite `dnf-plugins-core`.
> Vedi anche: `dnf`.
> Maggiori informazioni: <https://dnf-plugins-core.readthedocs.io/en/latest/changelog.html>.

- Visualizza tutti i changelog per un dato pacchetto:

`dnf changelog {{package}}`

- Visualizza tutti i changelog per un dato pacchetto dopo una data specificata:

`dnf changelog --since {{date}} {{package}}`

- Visualizza gli ultimi `n` changelog per un dato pacchetto:

`dnf changelog --count {{number}} {{package}}`

- Mostra solo i nuovi elementi per i pacchetti aggiornabili:

`dnf changelog --upgrades {{package}}`

- Mostra aiuto:

`dnf changelog --help-cmd`
