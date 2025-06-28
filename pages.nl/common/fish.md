# fish

> De Friendly Interactive SHell, een commandoregel-interpreteerder die is ontworpen voor gebruiksvriendelijkheid.
> Meer informatie: <https://fishshell.com>.

- Start een interactieve shell sessie:

`fish`

- Start een interactieve shell sessie zonder opstartconfiguraties te laden:

`fish --no-config`

- Voer specifieke commando's uit:

`fish --command "{{echo 'fish is executed'}}"`

- Voer een specifiek script uit:

`fish {{pad/naar/script.fish}}`

- Controleer een specifiek script op syntax fouten:

`fish --no-execute {{pad/naar/script.fish}}`

- Voer specifieke commando's uit van `stdin`:

`{{echo "echo 'fish is executed'"}} | fish`

- Start een interactieve shell sessie in privémodus, waarbij de shell geen toegang heeft tot oude geschiedenis of nieuwe geschiedenis opslaat:

`fish --private`

- Definieer en exporteer een omgevingsvariabele die blijft na het herstarten van de shell (ingebouwd):

`set --universal --export {{variabele_naam}} {{variabele_waarde}}`
