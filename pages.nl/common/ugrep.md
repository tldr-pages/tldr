# ugrep

> Ultrasnelle bestandszoeker met interactive UI.
> Meer informatie: <https://github.com/Genivia/ugrep>

- Open een interactieve TUI om recursief bestanden te zoeken (CTRL-Z help):

`ugrep -Q`

- Zoek recursief naar bestanden met inhoud die past bij een reguliere expressie patroon:

`ugrep "{{patroon}}"`

- Zoek recursief naar passende bestanden zonder voorkeur voor kleine- of hoofdletters:

`ugrep -i "{{patroon}}"`

- Geef een [l]ijst met passende bestanden:

`ugrep -l "{{patroon}}"`

- Zoek passende gecomprimeerde bestanden, [z]ip en tar archieven:

`ugrep -z "{{patroon}}"`

- Fu[z]zy zoeken met maximaal 3 extra, missende or verwisselende karakters in het patroon:

`ugrep -Z3 "{{patroon}}"`

- Zoek alleen bestanden met namen die overeenkomen met een passende [g]lob:

`ugrep -g "{{glob}}" "{{patroon}}"`

- Zoek alleen passende bestanden van een specifiek [t]ype of ander type en niet een derde type:

`ugrep -t {{type}},{{of_type}},^{{niet_type}} "{{patroon}}"`
