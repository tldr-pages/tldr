# acpi

> Muestra el estado de la batería o la información térmica.
> Más información: <https://manned.org/acpi>.

- Muestra la información de la batería:

`acpi`

- Muestra la información térmica:

`acpi {{[-t|--thermal]}}`

- Muestra la información del dispositivo de refrigeración:

`acpi {{[-c|--cooling]}}`

- Muestra la información térmica en Fahrenheit:

`acpi {{[-tf|--thermal --fahrenheit]}}`

- Muestra toda la información:

`acpi {{[-V|--everything]}}`

- Extrae la información de `/proc` en lugar de `/sys`:

`acpi {{[-p|--proc]}}`
