# history

> Beheer command-line geschiedenis.
> Meer informatie: <https://www.gnu.org/software/bash/manual/bash.html#index-history>.

- Toon de commandogeschiedenis met regelnummers:

`history`

- Toon de laatste 20 commando's (in Zsh worden alle commando's vanaf regel 20 vertoont):

`history 20`

- Toon geschiedenis met tijdstempels in verschillende formaten (alleen beschikbaar in Zsh):

`history -{{d|f|i|E}}`

- Wis ([c]) de commandogeschiedenis:

`history -c`

- Overschrijf ([w]) het geschiedenisbestand met de geschiedenis van de huidige Bash-shell (vaak gecombineerd met `history -c` om geschiedenis te wissen):

`history -w`

- Verwij[d]er een commando uit de geschiedenis op de opgegeven offset:

`history -d {{offset}}`

- Voeg een commando toe aan de geschiedenis zonder het uit te voeren:

`history -s {{commando}}`

- Voer een commando uit zonder het toe te voegen aan de geschiedenis door te beginnen met een spatie:

`<Spatie>{{command}}`
