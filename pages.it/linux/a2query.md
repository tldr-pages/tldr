# a2query

> Recupera la configurazione di runtime da Apache su sistemi operativi basati su Debian.
> Maggiori informazioni: <https://manpages.debian.org/latest/apache2/a2query.html>.

- Lista i moduli Apache attivi:

`sudo a2query -m`

- Controlla se un modulo specifico è installato:

`sudo a2query -m {{nome_modulo}}`

- Lista virtual host attivi:

`sudo a2query -s`

- Mostra il Modulo Multi-Processo correntemente attivo:

`sudo a2query -M`

- Mostra la versione di Apache:

`sudo a2query -v`
