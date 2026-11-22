# dnf download

> Scarica pacchetti RPM dai repository DNF.
> Non predefinito in `dnf` ma supportato tramite `dnf-plugins-core`.
> Maggiori informazioni: <https://dnf-plugins-core.readthedocs.io/en/latest/download.html>.

- Scarica l'ultima versione di un pacchetto nella directory corrente:

`dnf download {{pacchetto}}`

- Scarica un pacchetto in una directory specifica (la directory deve esistere):

`dnf download {{pacchetto}} --destdir {{percorso/della/directory}}`

- Stampa l'URL da cui scaricare il pacchetto RPM:

`dnf download --url {{pacchetto}}`
