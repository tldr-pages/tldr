# at

> Voer commando's één keer uit op een later tijdstip.
> Resultaten worden naar de e-mail van de gebruiker gestuurd.
> Meer informatie: <https://manned.org/at>.

- Maak commando's interactief en voer ze over 5 minuten uit (druk op `<Ctrl d>` wanneer klaar):

`at now + 5 minutes`

- Maak commando's interactief en voer ze uit op een specifiek tijdstip:

`at {{hh:mm}}`

- Voer een commando uit vanuit `stdin` om 10:00 uur vandaag:

`echo "{{commando}}" | at 1000`

- Voer commando's uit vanuit een opgegeven bestand volgende dinsdag:

`at -f {{pad/naar/bestand}} 9:30 PM Tue`

- Toon alle jobs in de wachtrij voor de huidige gebruiker (hetzelfde als `atq`):

`at -l`

- Toon een specifieke job:

`at -c {{job_nummer}}`
