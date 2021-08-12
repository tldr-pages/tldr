# balena

> Interacționați cu BalenaCloud, OpenBalena și API-ul balena din linia de comandă.
> Mai multe informaţii: <https://www.balena.io/docs/reference/cli/>

- Conectați-vă la contul BalenaCloud:

`balena login`

- Creați o aplicație BalenaCloud sau OpenBalena:

`balena app create {{app_name}}`

- Listează toate aplicațiile BalenaCloud sau OpenBalena din cont:

`balena apps`

- Afișați toate dispozitivele asociate contului BalenaCloud sau OpenBalena:

`balena devices`

- Flash o imagine BalenaOS la o unitate locală:

`balena local flash {{path/to/balenaos.img}} --drive {{drive_location}}`
