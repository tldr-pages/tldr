# xbps-remove

> XBPS hulpprogramma voor het verwijderen van pakketten.
> Zie ook: `xbps`.
> Meer informatie: <https://manned.org/xbps-remove.1>.

- Verwijder een pakket:

`xbps-remove {{pakket}}`

- Verwijder een pakket en zijn afhankelijkheden:

`xbps-remove {{[-R|--recursive]}} {{pakket}}`

- Verwijder verweesde pakketten (geïnstalleerd als afhankelijkheden, maar niet langer vereist door een pakket):

`xbps-remove {{[-o|--remove-orphans]}}`

- Verwijder verouderde pakketten van de cache:

`xbps-remove {{[-O|--clean-cache]}}`
