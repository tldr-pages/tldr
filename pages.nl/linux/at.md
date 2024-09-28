# at

> Voert commando's uit op een gespecificeerd tijdstip.
> Meer informatie: <https://manned.org/at.1>.

- Open een `at`-prompt om een nieuwe reeks geplande commando's te maken, druk op `Ctrl + D` om op te slaan en af te sluiten:

`at {{hh:mm}}`

- Voer de commando's uit en e-mail het resultaat met behulp van een lokaal mailprogramma zoals Sendmail:

`at {{hh:mm}} -m`

- Voer een script uit op het opgegeven tijdstip:

`at {{hh:mm}} -f {{pad/naar/bestand}}`

- Toon een systeembericht om 23:00 op 18 februari:

`echo "notify-send '{{Wake up!}}'" | at {{11pm}} {{Feb 18}}`
