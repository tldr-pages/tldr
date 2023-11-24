# crontab

> Plan cron jobs zodat deze volgens een tijdsinterval voor de huidige gebruiker worden uitgevoerd.
> Meer informatie: <https://crontab.guru/>.

- Pas het crontab bestand aan voor de huidige gebruiker:

`crontab -e`

- Pas het crontab bestand aan voor een specifieke gebruiker:

`sudo crontab -e -u {{gebruiker}}`

- Vervang de huidige crontab met de inhoud van een opgegeven bestand:

`crontab {{pad/naar/bestand}}`

- Bekijk een lijst van bestaande cron jobs voor de huidige gebruiker:

`crontab -l`

- Verwijder alle cron jobs voor de huidige gebruiker:

`crontab -r`

- Voorbeeld crontab entry, welke iedere dag om 10:00 draait (* betekent elke waarde):

`0 10 * * * {{commando_om_uit_te_voeren}}`

- Voorbeeld crontab entry, welke iedere 10 minuten een commando uitvoert:

`*/10 * * * * {{commando_om_uit_te_voeren}}`

- Voorbeeld crontab entry, welke iedere vrijdag om 02:30 een specifiek script draait:

`30 2 * * Fri {{/absoluut/pad/naar/script.sh}}`
