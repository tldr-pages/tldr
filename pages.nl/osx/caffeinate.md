# caffeinate

> Voorkom dat macOS in slaapstand gaat.
> Meer informatie: <https://keith.github.io/xcode-man-pages/caffeinate.8.html>.

- Voorkom slaapstand voor 1 uur (3600 seconden):

`caffeinate -u -t {{3600}}`

- Voorkom slaapstand totdat een commando is voltooid:

`caffeinate -s "{{commando}}"`

- Voorkom slaapstand totdat een proces met de opgegeven PID is voltooid:

`caffeinate -w {{pid}}`

- Voorkom slaapstand (gebruik `<Ctrl c>` om te stoppen):

`caffeinate -i`

- Voorkom dat de schijf in slaapstand gaat (gebruik `<Ctrl c>` om te stoppen):

`caffeinate -m`
