# shutdown

> Een tool om een machine af te sluiten, her op te starten of af te melden.
> Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/shutdown>.

- Sluit de huidige machine af:

`shutdown /s`

- Sluit de huidige machine af en sluit alle applicaties:

`shutdown /s /f`

- Herstart de huidige machine:

`shutdown /r /t 0`

- Zet de huidige machine in slaapstand:

`shutdown /h`

- Log uit van de huidige machine:

`shutdown /l`

- Zet een timer in aantal seconden voor het afsluiten van de huidige machine:

`shutdown /s /t {{seconden}}`

- Breek een afsluit sequentie af vooraleer de timer was afgelopen:

`shutdown /a`

- Sluit een machine af op afstand:

`shutdown /m {{\\hostnaam}}`
