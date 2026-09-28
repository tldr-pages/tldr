# fd

> Vind items in het bestandssysteem.
> Zie ook: `find`, `regex`.
> Meer informatie: <https://github.com/sharkdp/fd#command-line-options>.

- Vind recursief bestanden die overeenkomen met een specifiek patroon in de huidige map:

`fd "{{regex}}"`

- Vind bestanden in een specifieke map:

`fd "{{regex}}" {{pad/naar/map}}`

- Vind bestanden met een specifieke extensie:

`fd {{[-e|--extension]}} {{txt}}`

- Vind alleen mappen die overeenkomen met een specifiek patroon:

`fd "{{regex}}" {{[-t|--type]}} {{[d|directory]}}`

- Neem genegeerde en verborgen bestanden op in de zoekopdracht:

`fd "{{regex}}" {{[-HI|--hidden --no-ignore]}}`

- Sluit bestanden uit die overeenkomen met een specifiek `glob`-patroon:

`fd "{{regex}}" {{[-E|--exclude]}} {{glob}}`

- Voer een commando uit op elk zoekresultaat:

`fd "{{regex}}" {{[-x|--exec]}} {{commando}}`

- Vind bestanden alleen in de huidige map:

`fd "{{regex}}" {{[-d|--max-depth]}} 1`
