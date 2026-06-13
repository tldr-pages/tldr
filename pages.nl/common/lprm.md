# lprm

> Annuleer wachtende printtaken van een server.
> Zie ook: `lpq`.
> Meer informatie: <https://openprinting.github.io/cups/doc/man-lprm.html>.

- Annuleer de huidige taak op de standaard printer:

`lprm`

- Annuleer een taak van een specifieke server:

`lprm -h {{server}} {{taak_id}}`

- Annuleer een taak van een specifieke server op een specifieke poort:

`lprm -h {{server}}:{{poort}} {{taak_id}}`

- Annuleer meerdere taken met een beveiligde verbinding naar de server:

`lprm -E {{taak_id1 taak_id2 ...}}`

- Annuleer alle taken:

`lprm -`

- Annuleer de huidige taak van een specifieke printer of klasse:

`lprm -P {{bestemming}}/{{instantie]}}`
