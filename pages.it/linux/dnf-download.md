# dnf download

> Scarica pacchetti RPM dai repository DNF.
> Non predefinito in `dnf` ma supportato tramite `dnf-plugins-core`.
> Vedi anche: `dnf`.
> Maggiori informazioni: <https://dnf-plugins-core.readthedocs.io/en/latest/download.html>.

- Scarica l'ultima versione di un pacchetto nella directory corrente:

`dnf download {{package}}`

- Scarica un pacchetto in una directory specifica (la directory deve esistere):

`dnf download {{package}} --destdir {{path/to/directory}}`

- Stampa l'URL da cui scaricare il pacchetto RPM:

`dnf download --url {{package}}`
