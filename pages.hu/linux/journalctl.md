# journalctl

> A systemd napló lekérdezése. További információ: <https://manned.org/journalctl>.

- Az összes 3. prioritási szintű (hibás) üzenet megjelenítése ebből a \[b\]ootból:

`journalctl -b --priority={{3}}`

- Összes üzenet megjelenítése az utolsó \[b\]oot-ból:

`journalctl -b -1`

- A 2 napnál régebbi naplójegyzetek törlése:

`journalctl --vacuum-time={{2d}}`

- \[f\]ollow new messages (mint `tail -f` a hagyományos syslog esetében):

`journalctl -f`

- Az összes üzenet megjelenítése egy adott \[u\]nit:

`journalctl -u {{unit}}`

- Az üzenetek szűrése egy időintervallumon belül (időbélyegző vagy helyőrző, például "tegnap"):

`journalctl --since {{now|today|yesterday|tomorrow}} --until {{YYYY-MM-DD HH:MM:SS}}`

- Az összes üzenet megjelenítése egy adott folyamat szerint:

`journalctl _PID={{pid}}`

- Az összes üzenet megjelenítése egy adott futtatható program szerint:

`journalctl {{path/to/executable}}`
