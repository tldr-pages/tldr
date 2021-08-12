# useradd

> Creați un utilizator nou.
> Mai multe informaţii: <https://manned.org/useradd>

- Creați un utilizator nou:

`useradd {{name}}`

- Creați un utilizator nou cu un director de acasă implicit:

`useradd --create-home {{name}}`

- Creați un utilizator nou cu coajă specificată:

`useradd --shell {{path/to/shell}} {{name}}`

- Creați un utilizator nou aparținând unor grupuri suplimentare (minte lipsa de spațiu alb):

`useradd --groups {{group1,group2}} {{name}}`

- Creați un utilizator nou de sistem fără un director de acasă:

`useradd --no-create-home --system {{name}}`
