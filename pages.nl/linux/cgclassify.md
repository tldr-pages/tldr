# cgclassify

> Verplaats lopende taken naar opgegeven `cgroups`.
> Meer informatie: <https://manned.org/cgclassify>.

- Verplaats het proces met een specifiek PID naar de controle groep student in de CPU hierarchie:

`cgclassify -g {{cpu:student}} {{1234}}`

- Verplaats het proces met een specifiek PID naar de controle groepen gebaseerd op het `/etc/cgrules.conf` configuratie bestand:

`cgclassify {{1234}}`

- Verplaats het proces met een specifiek PID naar de controle groep student in de CPU hierarchy. Let op: de daemon van de service `cgred` veranderd `cgroups` van de specifieke PID en zijn onderliggende processen niet (gebaseerd op `/etc/cgrules.conf`):

`cgclassify --sticky -g {{cpu:/student}} {{1234}}`
