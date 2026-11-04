# glob

> `glob`-patronen zijn patronen die worden gebruikt om tekst te vergelijken en zoeken.
> Opmerking: `glob` is geen commando, maar syntax die gebruikt kan worden met andere commando's of de shell.
> Zie ook: `regex`.
> Meer informatie: <https://en.wikipedia.org/wiki/Glob_(programming)>.

- Zoek naar nul of meer van elk teken:

`*`

- Zoek naar één willekeurig teken:

`?`

- Zoek naar één teken uit een verzameling tekens:

`[{{abc}}]`

- Zoek naar reeksen van tekens:

`[{{a-z}}][{{3-9}}]`

- Zoek naar alles behalve het opgegeven teken:

`[!{{a}}]`

- Zoek naar een teken dat niet binnen een reeks valt:

`[!{{a-z}}]`
