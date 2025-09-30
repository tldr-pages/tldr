# vdir

> Toon uitgebreid de inhoud van een map.
> Vervanger voor `ls -l -b`.
> Meer informatie: <https://manned.org/vdir>.

- Toon bestanden en mappen in de huidige map, één per regel, met details:

`vdir`

- Toon met bestandsgroottes in mens-leesbare eenheden (KB, MB, GB):

`vdir {{[-h|--human-readable]}}`

- Toon inclusief verborgen bestanden (beginnend met een punt):

`vdir {{[-a|--all]}}`

- Toon bestanden en mappen gesorteerd op grootte (grootste eerst):

`vdir -S`

- Toon bestanden en mappen gesorteerd op wijzigingstijd (nieuwste eerst):

`vdir -t`

- Toon eerst mappen gegroepeerd:

`vdir --group-directories-first`

- Toon recursief alle bestanden en mappen in een specifieke map:

`vdir {{[-R|--recursive]}} {{pad/naar/map}}`
