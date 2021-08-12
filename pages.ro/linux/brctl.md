# brctl

> Administrarea punții Ethernet.
> Mai multe informaţii: <https://manned.org/brctl>

- Afișați o listă cu informații despre podurile ethernet existente în prezent:

`sudo brctl show`

- Creați o nouă interfață punte Ethernet:

`sudo brctl add {{bridge_name}}`

- Ștergeți o interfață punte ethernet existentă:

`sudo brctl del {{bridge_name}}`

- Adăugați o interfață la un pod existent:

`sudo brctl addif {{bridge_name}} {{interface_name}}`

- Eliminați o interfață de pe un pod existent:

`sudo brctl delif {{bridge_name}} {{interface_name}}`
