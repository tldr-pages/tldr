# clamav

> Antivirus de codi obert.
> Dissenyat especialment per escanejar correus electrònics, però pot ser emprat en altres contextos.
> Més informació: <https://www.clamav.net>.

- Actualitza definicions de virus:

`freshclam`

- Escaneja un arxiu en busca de virus:

`clamscan {{ruta/al/arxiu}}`

- Escaneja directoris recursivament i mostra els arxius infectats:

`clamscan --recursive --infected {{ruta/al/directori}}`

- Escaneja directoris recursivament y posa els arxius infectats en quarantena:

`clamscan --recursive --move={{directori}}`
