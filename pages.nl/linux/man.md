# man

> Formatteer en toon handleidingen.
> Meer informatie: <https://manned.org/man>.

- Toon de handleiding voor een commando:

`man {{commando}}`

- Open de handleiding voor een commando in een browser:

`man {{[-Hbrowser_name|--html=browser_name]}} {{commando}}`

- Toon de handleiding voor een commando uit sectie 7:

`man {{7}} {{commando}}`

- Toon alle beschikbare secties voor een commando:

`man {{[-f|--whatis]}} {{commando}}`

- Toon het pad dat wordt doorzocht voor handleidingen:

`man {{[-w|--path]}}`

- Toon de locatie van een handleiding in plaats van de handleiding zelf:

`man {{[-w|--where]}} {{commando}}`

- Toon de handleiding in een specifieke taal:

`man {{[-L|--locale]}} {{taal}} {{commando}}`

- Zoek naar handleidingen die een zoekterm bevatten:

`man {{[-k|--apropos]}} "{{zoekterm}}"`
