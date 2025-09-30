# kill

> Stuurt een signaal naar een proces, meestal om het proces te stoppen.
> Alle signalen behalve SIGKILL en SIGSTOP kunnen door het proces worden onderschept om een nette afsluiting uit te voeren.
> Meer informatie: <https://manned.org/kill.1posix>.

- Beëindig een programma met behulp van het standaard SIGTERM (terminate) signaal:

`kill {{proces_id}}`

- Toon beschikbare signalen (te gebruiken zonder het `SIG` voorvoegsel):

`kill -l`

- Beëindig een programma met behulp van het SIGHUP (hang up) signaal. Veel daemons zullen herladen in plaats van beëindigen:

`kill -{{1|HUP}} {{proces_id}}`

- Beëindig een programma met behulp van het SIGINT (interrupt) signaal. Dit wordt meestal geïnitieerd door de gebruiker die `<Ctrl c>` indrukt:

`kill -{{2|INT}} {{proces_id}}`

- Signaleer het besturingssysteem om een programma onmiddellijk te beëindigen (het programma krijgt geen kans om het signaal te onderscheppen):

`kill -{{9|KILL}} {{proces_id}}`

- Signaleer het besturingssysteem om een programma te pauzeren totdat een SIGCONT ("continue") signaal wordt ontvangen:

`kill -{{17|STOP}} {{proces_id}}`

- Stuur een `SIGUSR1` signaal naar alle processen met de gegeven GID (groeps-ID):

`kill -{{SIGUSR1}} -{{groep_id}}`
