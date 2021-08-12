# userdel

> Eliminați un cont de utilizator sau eliminați un utilizator dintr-un grup.
> Notă: toate comenzile trebuie executate ca root.
> Mai multe informaţii: <https://manned.org/userdel>

- Elimină un utilizator:

`userdel {{name}}`

- Eliminați un utilizator împreună cu directorul de acasă și bobina de poștă electronică:

`userdel --remove {{name}}`

- Eliminarea unui utilizator dintr-un grup:

`userdel {{name}} {{group}}`

- Eliminați un utilizator în alt director rădăcină:

`userdel --root {{path/to/other/root}} {{name}}`
