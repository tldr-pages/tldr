# prstat

> Raportează statistici despre procesele active.
> Mai multe informații: <https://www.unix.com/man-page/sunos/1m/prstat>.

- Examinează toate procesele și raportează statistici sortate după utilizarea CPU:

`prstat`

- Examinează toate procesele și raportează statistici sortate după utilizarea memoriei:

`prstat -s rss`

- Raportează un rezumat al utilizării totale pentru fiecare utilizator:

`prstat -t`

- Raportează informații despre microstările proceselor (microstate process accounting):

`prstat -m`

- Afișează o listă cu primele 5 procese consumatoare de CPU la fiecare secundă:

`prstat -c -n 5 -s cpu 1`
