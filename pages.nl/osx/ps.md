# ps

> Informatie over actieve processen.
> Meer informatie: <https://keith.github.io/xcode-man-pages/ps.1.html>.

- Toon alle actieve processen:

`ps aux`

- Toon alle actieve processen inclusief de volledige opdrachtregel:

`ps auxww`

- Zoek naar een proces dat overeenkomt met een string:

`ps aux | grep {{string}}`

- Verkrijg de parent PID van een proces:

`ps -o ppid= -p {{pid}}`

- Sorteer processen op geheugengebruik:

`ps -m`

- Sorteer processen op CPU-gebruik:

`ps -r`
