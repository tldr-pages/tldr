# acpi

> Zeigt den Akkustatus oder Temperatur-Informationen an.
> Weitere Informationen: <https://manned.org/acpi>.

- Zeige Informationen über den Akku an:

`acpi`

- Zeige Informationen zur Temperatur an:

`acpi {{[-t|--thermal]}}`

- Zeige Informationen über die Kühlung an:

`acpi {{[-c|--cooling]}}`

- Zeige Temperatur-Informationen in Fahrenheit an:

`acpi {{[-tf|--thermal --fahrenheit]}}`

- Zeige alle Informationen an:

`acpi {{[-V|--everything]}}`

- Extrahiere Informationen von `/proc`, anstatt von `/sys`:

`acpi {{[-p|--proc]}}`
