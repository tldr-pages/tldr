# netselect-apt

> Creați un fișier `sources.list` pentru o oglindă Debian cu cea mai mică latență.
> Mai multe informaţii: <https://manpages.debian.org/buster/netselect-apt/netselect-apt.1.html>

- Creaţi `sources.list` folosind cel mai mic server de latenţă:

`sudo netselect-apt`

- Specificați ramura Debian, stabil este utilizat în mod implicit:

`sudo netselect-apt {{testing}}`

- Includeți secțiunea nelibere:

`sudo netselect-apt --non-free`

- Specificați o țară pentru căutarea listei oglindă:

`sudo netselect-apt -c {{India}}`
