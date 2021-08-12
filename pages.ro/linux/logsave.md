# logsave

> Salvați ieșirea unei comenzi într-un fișier de jurnal.
> Mai multe informaţii: <https://manned.org/logsave>

- Executați comanda cu argumentele specificate și salvați ieșirea în fișierul jurnal:

`logsave {{path/to/logfile}} {{command}}`

- Luați intrarea de la intrarea standard și salvați-o într-un fișier jurnal:

`logsave {{logfile}} -`

- Adăugați ieșirea la un fișier jurnal, în loc să înlocuiți conținutul său curent:

`logsave -a {{logfile}} {{command}}`

- Afișează ieșirea verbose:

`logsave -v {{logfile}} {{command}}`
