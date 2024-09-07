# tar

> Archiveringsprogramma.
> Vaak gecombineerd met een compressiemethode, zoals `gzip` of `bzip2`.
> Meer informatie: <https://www.gnu.org/software/tar>.

- [c]reeër een archief en schrijf het naar een bestand ([f]):

`tar cf {{pad/naar/doel.tar}} {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- [c]reeër een g[z]ipt archief en schrijf het naar een bestand ([f]):

`tar czf {{pad/naar/doel.tar.gz}} {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- [c]reeër een g[z]ipt archief van een map met relatieve paden:

`tar czf {{pad/naar/doel.tar.gz}} --directory={{pad/naar/map}} .`

- E[x]traheer een (gecomprimeerd) archiefbestand ([f]) naar de huidige map [v]erbose:

`tar xvf {{pad/naar/bron.tar[.gz|.bz2|.xz]}}`

- E[x]traheer een (gecomprimeerd) archiefbestand ([f]) naar de doelmap:

`tar xf {{pad/naar/bron.tar[.gz|.bz2|.xz]}} --directory={{pad/naar/map}}`

- [c]reeër een gecomprimeerd archief en schrijf het naar een bestand ([f]), gebruikmakend van de bestandsnaam extensie om [a]utomatisch het compressieprogramma te bepalen:

`tar caf {{pad/naar/doel.tar.xz}} {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Lis[t] de inhoud van een tarbestand ([f]) [v]erbose:

`tar tvf {{pad/naar/bron.tar}}`

- E[x]traheer bestanden die overeenkomen met een patroon uit een archiefbestand ([f]):

`tar xf {{pad/naar/bron.tar}} --wildcards "{{*.html}}"`
