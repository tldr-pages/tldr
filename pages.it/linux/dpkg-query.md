# dpkg-query

> Uno strumento che mostra informazioni sui pacchetti installati.
> Maggiori informazioni: <https://manpages.debian.org/latest/dpkg/dpkg-query.1.html>.

- Elenca tutti i pacchetti installati:

`dpkg-query -l`

- Elenca i pacchetti installati con nomi che combaciano con una data espressione:

`dpkg-query -l '{{espressione_pattern}}'`

- Elenca tutti i file installati da una pacchetto:

`dpkg-query -L {{nome_del_pacchetto}}`

- Mostra le informazioni riguardanti un pacchetto:

`dpkg-query -s {{nome_del_pacchetto}}`
