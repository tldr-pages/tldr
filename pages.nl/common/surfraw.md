# surfraw

> Zoek in verschillende webzoekmachines.
> Bestaat uit een verzameling elvi's, die allemaal weten hoe ze een website moeten doorzoeken.
> Meer informatie: <https://manned.org/surfraw>.

- Toon de ondersteunde websitezoekscripts (elvi):

`surfraw -elvi`

- Open de resultatenpagina van de elvi voor een specifieke zoekopdracht in de browser:

`surfraw {{elvi_naam}} "{{zoektermen}}"`

- Toon een elvi-beschijving en zijn specifieke opties:

`surfraw {{elvi_naam}} {{[-lh|-local-help]}}`

- Zoek met behulp van een elvi met specifieke opties en open de resultatenpagina in de browser:

`surfraw {{elvi_naam}} {{elvi_opties}} "{{zoektermen}}"`

- Toon de URL van de resultatenpagina van de elvi voor een specifieke zoekopdracht:

`surfraw -print {{elvi_naam}} "{{zoektermen}}"`

- Zoek met de alias:

`sr {{elvi_naam}} "{{zoektermen}}"`
