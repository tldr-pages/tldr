# ps

> Informatie over actieve processen.
> Meer informatie: <https://manned.org/ps>.

- Toon alle actieve processen:

`ps aux`

- Toon alle actieve processen inclusief de volledige commandoregel:

`ps auxww`

- Zoek naar een proces dat overeenkomt met een string (de vierkante haken voorkomen dat `grep` zichzelf vindt):

`ps aux | grep {{[s]tring}}`

- Toon alle processen van de huidige gebruiker in extra volledig formaat:

`ps --user $(id -u) -F`

- Toon alle processen van de huidige gebruiker als een boomstructuur:

`ps --user $(id -u) f`

- Verkrijg de parent PID van een proces:

`ps -o ppid= -p {{pid}}`

- Sorteer processen op geheugengebruik:

`ps --sort size`
