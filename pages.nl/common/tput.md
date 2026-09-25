# tput

> Bekijk en wijzig terminalinstellingen en -mogelijkheden.
> Zie ook: `stty`.
> Meer informatie: <https://manned.org/tput>.

- Verplaats de cursor naar een schermlocatie:

`tput cup {{rij}} {{kolom}}`

- Stel de voorgrond- (af) of achtergrondkleur (ab) in:

`tput {{setaf|setab}} {{ansi_kleurcode}}`

- Verwissel tekst- en achtergrondkleuren:

`tput rev`

- Reset alle tekstattributen van de terminal:

`tput sgr0`

- Toon het aantal kolommen, regels of kleuren:

`tput {{cols|lines|colors}}`

- Schakel woordafbreking in of uit:

`tput {{smam|rmam}}`

- Verberg of toon de terminalcursor:

`tput {{civis|cnorm}}`

- Sla de tekststatus van de terminal op of herstel deze (smcup legt ook scrollwielgebeurtenissen vast):

`tput {{smcup|rmcup}}`
