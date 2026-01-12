# bzgrep

> Zoek patronen in `bzip2` gecomprimeerde bestanden met behulp van `grep`.
> Meer informatie: <https://manned.org/bzgrep>.

- Zoek naar een patroon in een gecomprimeerd bestand:

`bzgrep "{{zoekpatroon}}" {{pad/naar/bestand}}`

- Zoek recursief naar een patroon in bestanden in een bzip2 gecomprimeerd `.tar`-archief:

`bzgrep {{[-r|--recursive]}} "{{zoekpatroon}}" {{pad/naar/tar_bestand}}`

- Toon 3 regels rondom [C]ontext, voor ([B]) of  na ([A]) elke overeenkomst:

`bzgrep {{--context|--before-context|--after-context}} 3 "{{zoekpatroon}}" {{pad/naar/bestand}}`

- Toon de bestandsnaam en het regelnummer voor elke overeenkomst:

`bzgrep {{[-H|--with-filename]}} {{[-n|--line-number]}} "{{zoekpatroon}}" {{pad/naar/bestand}}`

- Zoek naar regels die overeenkomen met een patroon en geef alleen de overeenkomende tekst weer:

`bzgrep {{[-o|--only-matching]}} "{{zoekpatroon}}" {{pad/naar/bestand}}`

- Zoek in `stdin` naar regels die niet overeenkomen met een patroon:

`cat {{pad/naar/bz_gecomprimeerd_bestand}} | bzgrep {{[-v|--invert-match]}} "{{zoekpatroon}}"`

- Gebruik uitgebreide `regex` (ondersteunt `?`, `+`, `{}`, `()` en `|`), in hoofdletterongevoelige modus:

`bzgrep {{[-E|--extended-regexp]}} {{[-i|--ignore-case]}} "{{zoekpatroon}}" {{pad/naar/bestand}}`
