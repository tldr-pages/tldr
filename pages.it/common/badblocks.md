# badblocks

> Cerca blocchi danneggiati su un dispositivo.
> Alcuni utilizzi di `badblocks` possono causare azioni distruttive, come la cancellazione di tutti i dati su un disco, inclusa la tabella delle partizioni.
> Maggiori informazioni: <https://manned.org/badblocks>.

- Cerca blocchi danneggiati su un disco con test di sola [l]ettura non distruttivo:

`sudo badblocks {{/dev/sdX}}`

- Cerca blocchi danneggiati su un disco [n]on montato con test di lettura-scrittura non distruttivo:

`sudo badblocks -n {{/dev/sdX}}`

- Cerca blocchi danneggiati su un disco [n]on montato con test di [s]crittura distruttivo:

`sudo badblocks -w {{/dev/sdX}}`

- Usa il test di [s]crittura distruttivo e mostra il [p]rogresso [v]erboso:

`sudo badblocks -svw {{/dev/sdX}}`

- In modalità distruttiva, [s]alva i blocchi trovati in un file:

`sudo badblocks -o {{percorso/al/file}} -w {{/dev/sdX}}`

- Usa modalità distruttiva con velocità migliorata: dimensione blocco 4K e [c]ount blocchi 64K:

`sudo badblocks -w -b {{4096}} -c {{65536}} {{/dev/sdX}}`
