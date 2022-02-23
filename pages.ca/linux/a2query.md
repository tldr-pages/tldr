# a2query

> Recupera la configuració del temps d'execució d'Apache en sistemes operatius basats en Debian.
> Més informació: <https://manpages.debian.org/latest/apache2/a2query.html>.

- Llista mòduls Apache activats:

`sudo a2query -m`

- Comprova si un mòdul específic està instal·lat:

`sudo a2query -m {{nom_mòdul}}`

- Llista els hosts virtuals activats:

`sudo a2query -s`

- Mostra el mòdul de processament múltiple:

`sudo a2query -M`

- Mostra la versió d'Apache:

`sudo a2query -v`
