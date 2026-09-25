# run-mailcap

> Voer programma's uit via vermeldingen in het mailcap-bestand.
> Meer informatie: <https://manned.org/run-mailcap>.

- Bewerk een bestaand of nieuw bestand met de standaard `mailcap`-bewerktool:

`run-mailcap --action=compose {{pad/naar/bestand}}`

- Bekijk een bestand met de standaard `mailcap`-verkenner:

`run-mailcap --action=edit {{pad/naar/bestand}}`

- Print een bestand met de standaard `mailcap`-printtool:

`run-mailcap --action=print {{pad/naar/bestand}}`

- Bekijk een bestand (meestal een afbeelding) met de standaard `mailcap`-verkenner:

`run-mailcap --action=view {{pad/naar/bestand}}`

- Roep afzonderlijke acties/programma's aan via run-mailcap:

`run-mailcap --action={{view|cat|compose|composetyped|edit|print}} {{pad/naar/bestand}}`

- Schakel extra informatie in:

`run-mailcap --action={{actie}} --debug {{pad/naar/bestand}}`

- Negeer elke "copiousoutput"-richtlijn en stuur de uitvoer door naar `stdout`:

`run-mailcap --action={{actie}} --nopager {{pad/naar/bestand}}`

- Toon het gevonden commando zonder het daadwerkelijk uit te voeren:

`run-mailcap --action={{actie}} --norun {{pad/naar/bestand}}`
