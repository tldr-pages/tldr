# adduser

> Utilitar de adăugare utilizator.
> Mai multe informaţii: <https://manpages.debian.org/latest/adduser/adduser.html>

- Creați un utilizator nou cu un director de acasă implicit și solicitați utilizatorului să seteze o parolă:

`adduser {{username}}`

- Creați un utilizator nou fără un director de acasă:

`adduser --no-create-home {{username}}`

- Creați un utilizator nou cu un director de acasă la calea specificată:

`adduser --home {{path/to/home}} {{username}}`

- Creați un utilizator nou cu setul de coajă specificat ca coajă de conectare:

`adduser --shell {{path/to/shell}} {{username}}`

- Creați un utilizator nou aparținând grupului specificat:

`adduser --ingroup {{group}} {{username}}`

- Adăugați un utilizator existent la grupul specificat:

`adduser {{username}} {{group}}`
