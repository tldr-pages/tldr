# ugrep

> Ultrasnelle bestandszoeker met interactive UI.
> Meer informatie: <https://github.com/Genivia/ugrep>.

- Open een interactieve TUI om recursief bestanden te zoeken (`<Ctrl z>` voor hulp):

`ugrep {{[-Q|--query]}}`

- Zoek recursief met een regex zoekpatroon in de huidige map naar passende bestanden:

`ugrep "{{zoekpatroon}}"`

- Zoek een gegeven bestand of bestanden in een gegeven map en laat de passende regelnummers zien:

`ugrep {{[-n|--line-number]}} "{{zoekpatroon}}" {{pad/naar/bestand_of_map}}`

- Zoek recursief in de huidige map en geef een lijst met passende bestanden:

`ugrep {{[-l|--files-with-matches]}} "{{zoekpatroon}}"`

- Zoek "fuzzy" met maximaal 3 extra, missende of verwisselende karakters in het patroon:

`ugrep {{[-Z|--fuzzy=]}}{{3}} "{{zoekpatroon}}"`

- Zoek passende gecomprimeerde bestanden, zip en tar archieven recursief in de huidige map:

`ugrep {{[-z|--decompress]}} "{{zoekpatroon}}"`

- Zoek alleen naar bestanden met namen die overeenkomen met een specifieke glob patroon:

`ugrep {{[-g |--glob=]}}"{{glob_patroon}}" "{{zoekpatroon}}"`

- Zoek alleen passende bestanden van het type C++ (gebruik `--type=list` voor een lijst van typenamen):

`ugrep {{[-t |--file-type=]}}cpp "{{zoekpatroon}}"`
