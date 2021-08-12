# snap

> Instrument pentru gestionarea pachetelor software autonome „snap”.
> Similar cu ceea ce înseamnă `apt` pentru „.deb”.

- Caută un pachet:

`snap find {{package_name}}`

- Instalați un pachet:

`snap install {{package_name}}`

- Actualizarea unui pachet:

`snap refresh {{package_name}}`

- Actualizați un pachet pe un alt canal (pistă, risc sau ramură):

`snap refresh {{package_name}} --channel={{channel}}`

- Actualizaţi toate pachetele:

`snap refresh`

- Afișați informații de bază despre software-ul snap instalat:

`snap list`

- Dezinstalați un pachet:

`snap remove {{package_name}}`

- Verificați dacă există modificări recente ale sistemului:

`snap changes`
