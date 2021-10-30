# shutdown

> Spegni e riavvia il sistema.
> Maggiori informazioni: <https://manned.org/shutdown.8>.

- Spegni il sistema immediatamente:

`shutdown -h now`

- Riavvia il sistema immediatamente:

`shutdown -r now`

- Riavvia il sistema in 5 minuti:

`shutdown -r +{{5}} &`

- Spegni il sistema alle 13:

`shutdown -h 13:00`

- Annulla un'operazione programmata di riavvio o spegnimento:

`shutdown -c`
