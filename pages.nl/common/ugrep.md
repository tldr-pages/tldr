# ugrep

> Ultrasnelle bestandszoeker met interactive UI.
> Meer informatie: <https://github.com/Genivia/ugrep>.

- Open een interactieve TUI om recursief bestanden te zoeken (CTRL-Z voor hulp):

`ugrep --query`

- Zoek recursief met een regex zoekpatroon in de huidige directory naar passende bestanden:

`ugrep "{{zoekpatroon}}"`

- Zoek een gegeven bestand of bestanden in een gegeven directory en laat de passende regelnummers zien:

`ugrep --line-number "{{zoekpatroon}}" {{pad/naar/bestand_of_directory}}`

- Zoek recursief in de huidige directory en geef een lijst met passende bestanden:

`ugrep --files-with-matches "{{zoekpatroon}}"`

- Zoek "fuzzy" met maximaal 3 extra, missende of verwisselende karakters in het patroon:

`ugrep --fuzzy=3 "{{zoekpatroon}}"`

- Zoek passende gecomprimeerde bestanden, zip en tar archieven recursief in de huidige directory:

`ugrep --decompress "{{zoekpatroon}}"`

- Zoek alleen naar bestanden met namen die overeenkomen met een passende `foo*.???` glob patroon:

`ugrep --glob="{{foo*.???}}" "{{zoekpatroon}}"`

- Zoek alleen passende bestanden van het type C++ (gebruik `--type=list` voor een lijst van typenamen):

`ugrep --type=cpp "{{zoekpatroon}}"`
