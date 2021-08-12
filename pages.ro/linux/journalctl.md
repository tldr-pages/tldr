# journalctl

> Interogare jurnal systemd.

- Afișează toate mesajele din această [b] oot:

`journalctl -b`

- Afișează toate mesajele din ultima [b] oot:

`journalctl -b -1`

- Afișează toate mesajele cu nivel de prioritate 3 (erori) din această [b] oot:

`journalctl -b --priority={{3}}`

- [f] mesaje noi ollow (cum ar fi `tail -f` pentru syslog tradițional):

`journalctl -f`

- Afișează toate mesajele printr-un anumit [u] nit:

`journalctl -u {{unit}}`

- Filtrarea mesajelor într-un interval de timp (fie marcaj temporal, fie substituenți, cum ar fi „ieri”):

`journalctl --since {{now|today|yesterday|tomorrow}} --until {{YYYY-MM-DD HH:MM:SS}}`

- Afișați toate mesajele printr-un anumit proces:

`journalctl _PID={{pid}}`

- Afișează toate mesajele printr-un executabil specific:

`journalctl {{path/to/executable}}`
