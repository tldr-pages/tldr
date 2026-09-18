# pw-dump

> Scarica lo stato corrente di PipeWire come JSON, incluse le informazioni su nodi, dispositivi, moduli, porte e altri oggetti.
> Vedi anche: `pw-mon`.
> Maggiori informazioni: <https://docs.pipewire.org/page_man_pw-dump_1.html>.

- Stampa una rappresentazione JSON dello stato corrente dell'istanza PipeWire predefinita:

`pw-dump`

- Stampa una rappresentazione JSON di un oggetto:

`pw-dump {{id_oggetto}}`

- Scarica lo stato corrente monitorando i cambiamenti, stampandolo nuovamente:

`pw-dump {{[-m|--monitor]}}`

- Scarica lo stato corrente di un'istanza remota in un file:

`pw-dump {{[-r|--remote]}} {{nome_remoto}} > {{percorso/file_dump.json}}`

- Imposta una configurazione colore:

`pw-dump {{[-C|--color]}} {{never|always|auto}}`

- Mostra aiuto:

`pw-dump {{[-h|--help]}}`
