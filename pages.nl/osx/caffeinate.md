# caffeinate

> Voorkom dat macOS in slaapstand gaat.
> Meer informatie: <https://keith.github.io/xcode-man-pages/caffeinate.8.html>.

- Voorkom dat het scherm in slaapstand gaat:

`caffeinate -d`

- Voorkom dat het scherm gedurende 1 uur (3600 seconden) in slaapstand gaat:

`caffeinate -u -t {{3600}}`

- Splits een proces, voer daarin "make" uit en voorkom dat het scherm in slaapstand gaat zolang dat proces actief is:

`caffeinate -i make`

- Voorkom dat het scherm in slaapstand gaat totdat een proces met het opgegeven PID is voltooid:

`caffeinate -w {{pid}}`

- Voorkom dat de schijf in slaapstand gaat (gebruik `<Ctrl c>` om te stoppen):

`caffeinate -m`
