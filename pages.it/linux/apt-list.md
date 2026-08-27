# apt list

> Elenca i pacchetti.
> Nota: si consiglia di eseguire `apt update` prima per aggiornare i file dell'indice dei pacchetti locali.
> Maggiori informazioni: <https://manned.org/apt.8>.

- Elenca tutti i pacchetti disponibili:

`apt list`

- Elenca i pacchetti solo per nome (supporta wildcard come *):

`apt list {{pacchetto}}`

- Elenca i pacchetti installati:

`apt list {{[-i|--installed]}}`

- Elenca i pacchetti aggiornabili:

`apt list {{[-u|--upgradable]}}`
