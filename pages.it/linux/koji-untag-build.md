# koji untag-build

> Rimuove un tag da una o più build.
> Maggiori informazioni: <https://docs.pagure.org/koji/>.

- Rimuove un tag da una o più build:

`koji untag-build {{tag}} {{NVR1 NVR2 ...}}`

- Rimuovi il tag da tutte le versioni del pacchetto in questo tag:

`koji untag-build {{tag}} {{pkg1 pkg2 ...}} --all`

- Rimuovi il tag da tutte le versioni del pacchetto in questo tag tranne l'ultima:

`koji untag-build {{tag}} {{pkg1 pkg2 ...}} --non-latest`

- Modalità di prova:

`koji untag-build {{tag}} {{NVR1 NVR2 ...}} {{[-n|--test]}}`

- Stampa dettagli:

`koji untag-build {{tag}} {{NVR1 NVR2 ...}} {{[-v|--verbose]}}`

- Mostra aiuto:

`koji untag-build {{[-h|--help]}}`
