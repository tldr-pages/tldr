# killall

> Verstuur een kill-signaal naar alle instanties van een proces op naam (moet exact overeenkomen).
> Alle signalen behalve SIGKILL en SIGSTOP kunnen door het proces worden onderschept, waardoor een nette afsluiting mogelijk is.
> Meer informatie: <https://manned.org/killall>.

- Beëindig een proces met behulp van het standaard SIGTERM (terminate) signaal:

`killall {{proces_naam}}`

- [l]ijst beschikbare signaalnamen (te gebruiken zonder het 'SIG'-voorvoegsel):

`killall -l`

- Vraag interactief om bevestiging voordat het proces wordt beëindigd:

`killall -i {{proces_naam}}`

- Beëindig een proces met het SIGINT (interrupt) signaal, hetzelfde signaal dat wordt verzonden door `<Ctrl c>` in te drukken:

`killall -INT {{proces_naam}}`

- Forceer het beëindigen van een proces:

`killall -KILL {{proces_naam}}`
