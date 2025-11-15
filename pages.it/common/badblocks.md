# badblocks

> Cerca blocchi corrotti in un dispositivo.
> Alcuni utilizzi di badblocks possono avere esiti non reversibili, come perdita dei dati o anche della tabella delle partizioni di un disco.
> Maggiori informazioni: <https://manned.org/badblocks>.

- Cerca blocchi corrotti in un disco utilizzando un test non distruttivo in sola lettura:

`sudo badblocks {{/dev/sda}}`

- Cerca blocchi corrotti in un disco non montato con un test non distruttivo in lettura e scrittura:

`sudo badblocks -n {{/dev/sda}}`

- Cerca blocchi corrotti in un disco non montato con un test distruttivo in scrittura:

`sudo badblocks -w {{/dev/sda}}`
