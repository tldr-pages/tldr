# stat

> Toon bestandsstatus.
> Meer informatie: <https://keith.github.io/xcode-man-pages/stat.1.html>.

- Toon bestandseigenschappen zoals grootte, permissies, aanmaak- en toegangsdatums en meer:

`stat {{pad/naar/bestand}}`

- Zelfde als hierboven maar uitgebreid (meer vergelijkbaar met Linux's `stat`):

`stat -x {{pad/naar/bestand}}`

- Toon alleen octale bestandspermissies:

`stat -f %Mp%Lp {{pad/naar/bestand}}`

- Toon eigenaar en groep van het bestand:

`stat -f "%Su %Sg" {{pad/naar/bestand}}`

- Toon de grootte van het bestand in bytes:

`stat -f "%z %N" {{pad/naar/bestand}}`
