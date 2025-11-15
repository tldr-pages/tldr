# ed

> De originele Unix tekst editor.
> Zie ook: `awk`, `sed`.
> Meer informatie: <https://www.gnu.org/software/ed/manual/ed_manual.html>.

- Start een interactieve editor sessie met een leeg document:

`ed`

- Start een interactieve editor sessie met een leeg document en een specifieke prompt:

`ed {{[-p|--prompt]}} '{{> }}'`

- Start een interactieve editor sessie met gebruiksvriendelijke foutmeldingen:

`ed {{[-v|--verbose]}}`

- Start een interactieve editor sessie met een leeg document en zonder diagnostics, het aantal bytes en de '!' prompt:

`ed {{[-q|--quiet]}} {{[-s|--script]}}`

- Start een interactieve editor sessie zonder exit status change als het commando faalt:

`ed {{[-l|--loose-exit-status]}}`

- Pas een specifiek bestand aan (dit toont het aantal bytes van het geladen bestand):

`ed {{pad/naar/bestand}}`

- Vervang een string met een specifieke vervanging voor alle regels:

`,s/{{reguliere_expressie}}/{{vervanging}}/g<Enter>`

- Sluit `ed` af:

`q<Enter>`
