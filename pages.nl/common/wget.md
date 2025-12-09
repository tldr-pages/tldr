# wget

> Download bestanden vanaf het internet.
> Ondersteunt HTTP, HTTPS en FTP.
> Meer informatie: <https://www.gnu.org/software/wget/manual/wget.html>.

- Download de inhoud van een URL naar een bestand (in dit geval genaamd "foo"):

`wget {{https://example.com/foo}}`

- Download de inhoud van een URL naar een bestand (in dit geval genaamd "bar"):

`wget {{[-O|--output-document]}} {{bar}} {{https://example.com/foo}}`

- Download één webpagina en alle bijbehorende bronnen met een interval van 3 seconden tussen verzoeken (scripts, stylesheets, afbeeldingen, etc.):

`wget {{[-pkw|--page-requisites --convert-links --wait]}} 3 {{https://example.com/een_pagina.html}}`

- Download alle vermelde bestanden binnen een map en zijn submappen (downloadt geen embedded pagina-elementen):

`wget {{[-mnp|--mirror --no-parent]}} {{https://example.com/een_pad/}}`

- Beperk de downloadsnelheid en het aantal verbindingspogingen:

`wget --limit-rate {{300k}} {{[-t|--tries]}} {{100}} {{https://example.com/een_pad/}}`

- Download een bestand van een HTTP-server met behulp van Basic Auth (werkt ook met FTP):

`wget --user {{gebruikersnaam}} --password {{wachtwoord}} {{https://example.com}}`

- Hervat een onvolledige download:

`wget {{[-c|--continue]}} {{https://example.com}}`

- Download alle URL's die zijn opgeslagen in een tekstbestand naar een specifieke map:

`wget {{[-P|--directory-prefix]}} {{pad/naar/map}} {{[-i|--input-file]}} {{pad/naar/URLs.txt}}`
