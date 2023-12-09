# ar

> Maken, aanpassen en uitpakken van Unix archieven. Typisch gebruikt voor statische bibliotheken (`.a`) en Debian pakketten (`.deb`).
> Bekijk ook: `tar`.
> Meer informatie: <https://manned.org/ar>.

- Pak alles uit van een archief:

`ar x {{pad/naar/bestand.a}}`

- [t]oon inhoud van een specifiek archief:

`ar t {{pad/naar/bestand.ar}}`

- Ve[r]vang of voeg specifieke bestanden toe aan een archief:

`ar r {{pad/naar/bestand.deb}} {{pad/naar/debian-binary pad/naar/control.tar.gz pad/naar/data.tar.xz ...}}`

- Voeg een object bestandsindex toe (equivalent aan het gebruik van `ranlib`):

`ar s {{pad/naar/bestand.a}}`

- Maak een archief met specifieke bestanden en een begeleidend object bestandsindex:

`ar rs {{pad/naar/bestand.a}} {{pad/naar/bestand1.o pad/naar/bestand2.o ...}}`
