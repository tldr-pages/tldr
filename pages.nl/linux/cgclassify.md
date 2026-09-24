# cgclassify

> Verplaats lopende taken naar `cgroups`.
> Meer informatie: <https://manned.org/cgclassify>.

- Verplaats het proces met een specifiek PID naar de controlegroep student in de CPU-hiërarchie:

`cgclassify -g {{cpu:student}} {{1234}}`

- Verplaats het proces met een specifiek PID naar de controlegroepen gebaseerd op het `/etc/cgrules.conf` configuratiebestand:

`cgclassify {{1234}}`

- Verplaats het proces met een specifiek PID naar de controlegroep student in de CPU-hiërarchie. Let op: de daemon van de service `cgred` verandert `cgroups` van de specifieke PID en zijn onderliggende processen niet (gebaseerd op `/etc/cgrules.conf`):

`cgclassify --sticky -g {{cpu:/student}} {{1234}}`
