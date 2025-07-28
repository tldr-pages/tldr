# fish

> De Friendly Interactive SHell, een commandoregel-interpreteerder die is ontworpen voor gebruiksvriendelijkheid.
> Meer informatie: <https://fishshell.com/docs/current/cmds/fish.html>.

- Start een interactieve shell sessie:

`fish`

- Start een interactieve shell sessie zonder opstartconfiguraties te laden:

`fish {{[-N|--no-config]}}`

- Voer specifieke commando's uit:

`fish {{[-c|--command]}} "{{echo 'fish is executed'}}"`

- Voer een specifiek script uit:

`fish {{pad/naar/script.fish}}`

- Controleer een specifiek script op syntax fouten:

`fish {{[-N|--no-execute]}} {{pad/naar/script.fish}}`

- Voer specifieke commando's uit van `stdin`:

`{{echo "echo 'fish is executed'"}} | fish`

- Start een interactieve shell sessie in privémodus, waarbij de shell geen toegang heeft tot oude geschiedenis of nieuwe geschiedenis opslaat:

`fish {{[-P|--private]}}`

- Definieer en exporteer een omgevingsvariabele die blijft na het herstarten van de shell (ingebouwd):

`set {{[-U|--universal]}} {{[-x|--export]}} {{variabele_naam}} {{variabele_waarde}}`
