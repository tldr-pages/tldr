# mail

> Werk met de mailbox van de gebruiker.
> Om een e-mail te versturen wordt de berichttekst opgebouwd vanaf `stdin`.
> Meer informatie: <https://manned.org/mail>.

- Open een interactieve prompt om persoonlijke mail te bekijken:

`mail`

- Verstuur een getypt e-mailbericht met optionele CC. Het onderstaande commando gaat verder na het indrukken van `<Enter>`. Voer de berichttekst in (kan meerdere regels bevatten). Druk op `<Ctrl d>` om de berichttekst af te ronden:

`mail --subject "{{onderwerpregel}}" {{to_user@example.com}} --cc "{{cc_email_adres}}"`

- Verstuur een e-mail met de inhoud van een bestand:

`mail < {{pad/naar/bestand.txt}} --subject "{{$HOSTNAME bestandsnaam.txt}}" {{to_user@example.com}}`

- Verstuur een `.tar.gz` bestand als bijlage:

`tar cvzf - {{pad/naar/map1 pad/naar/map2}} | uuencode {{data.tar.gz}} | mail --subject "{{onderwerpregel}}" {{to_user@example.com}}`

- Toon de help:

`mail {{[-h|--help]}}`
