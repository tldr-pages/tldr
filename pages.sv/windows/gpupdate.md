# gpupdate

> Ett verktyg för att kontrollera och uppdatera Windows Group Policy settings.
> Mer information: <https://learn.microsoft.com/windows-server/administration/windows-commands/gpupdate>.

- Kontrollera och tillämpa uppdaterade Group Policy settings:

`gpupdate`

- Ange för vilka Group Policy inställningar du vill kontrollera för uppdateringar:

`gpupdate /target:{{datornamn|användare}}`

- Tvinga alla Group Policy inställningar att tillämpas igen:

`gpupdate /force`

- Visa detaljerad användningsinformation:

`gpupdate /?`
