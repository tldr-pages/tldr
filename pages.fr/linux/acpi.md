# acpi

> Affiche l'état de la batterie ou des renseignements sur la température.
> Plus d'informations : <https://manned.org/acpi>.

- Affiche les informations sur la batterie :

`acpi`

- Affiche les informations sur la température :

`acpi {{[-t|--thermal]}}`

- Affiche les informations sur le dispositif de refroidissement :

`acpi {{[-c|--cooling]}}`

- Affiche les informations sur le dispositif de refroidissement en Fahrenheit :

`acpi {{[-tf|--thermal --fahrenheit]}}`

- Affiche toutes les informations :

`acpi {{[-V|--everything]}}`

- Extrait les informations depuis `/proc` au lieu de `/sys` :

`acpi {{[-p|--proc]}}`
