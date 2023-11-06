# xbps-remove

> XBPS hulpprogramma voor het verwijderen van pakketten.
> Bekijk ook: `xbps`.
> Meer informatie: <https://man.voidlinux.org/xbps-remove.1>.

- Verwijder een pakket:

`xbps-remove {{pakket}}`

- Verwijder een pakket en zijn afhankelijkheden:

`xbps-remove --recursive {{pakket}}`

- Verwijder verweesde pakketten (geïnstalleerd als afhankelijkheden, maar niet langer vereist door een pakket):

`xbps-remove --remove-orphans`

- Verwijder verouderde pakketten van de cache:

`xbps-remove --clean-cache`
