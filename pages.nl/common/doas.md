# doas

> Voer een commando uit als een andere gebruiker.
> Meer informatie: <https://man.openbsd.org/doas>.

- Voer een commando uit als root:

`doas {{command}}`

- Voer een commando uit als een andere gebruiker:

`doas -u {{gebruiker}} {{commando}}`

- Start de standaard shell als root:

`doas -s`

- Parse een configuratiebestand en controleer of de uitvoering van het commando als een andere gebruiker toegestaan is:

`doas -C {{pad/naar/configuratiebestand}} {{command}}`

- Zorg ervoor dat `doas` om een wachtwoord vraagt, zelfs als het eerder is opgegeven:

`doas -L`
