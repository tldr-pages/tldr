# flock

> Beheer bestandslocks van shell scripts.
> Het kan gebruikt worden om ervoor te zorgen dat slechts één instantie van een commando draait.
> Meer informatie: <https://manned.org/flock>.

- Voer een commando met een bestandslock uit zodra de lock beschikbaar is:

`flock {{pad/naar/lock.lock}} {{commando}}`

- Voer een opdracht uit met een bestandslock, of sluit het programma af als de lock momenteel actief is (met foutcode 1):

`flock {{pad/naar/lock.lock}} {{[-n|--nonblock]}} {{commando}}`

- Voer een opdracht uit met een bestandslock, of sluit af met een specifieke foutcode als de lock momenteel actief is:

`flock {{pad/naar/lock.lock}} {{[-n|--nonblock]}} {{[-E|--conflict-exit-code]}} {{123}} {{commando}}`

- Voer een commando uit met een bestandslock en wacht maximaal 10 seconden tot de lock beschikbaar is voordat wordt opgegeven:

`flock {{pad/naar/lock.lock}} {{[-w|--timeout]}} 10 {{commando}}`

- Maak een back-up van een aantal bestanden, wacht tot het vorige `tar`-commando klaar is als deze nog wordt uitgevoerd en houd dezelfde bestandlock vast (kan gebruikt worden in een `cron` job die periodiek wordt uitgevoerd):

`flock {{pad/naar/backup.lock}} {{tar -cvf pad/naar/backup.tar pad/naar/data/}}`
