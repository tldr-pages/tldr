# memray

> Houd geheugengebruik bij van een Python-applicatie.
> Meer informatie: <https://github.com/bloomberg/memray#usage>.

- Voer een Python-bestand uit en houd het geheugengebruik bij:

`memray run {{pad/naar/bestand}}.py`

- Voer een [m]odule uit en houd het geheugengebruik bij:

`memray run -m {{module_naam}}`

- Geef een uitvoernaam op:

`memray run {{[-o|--output]}} {{pad/naar/uitvoerbestand}}.bin {{pad/naar/bestand}}.py`

- Toon een samenvatting van het geheugengebruik:

`memray summary {{pad/naar/bestand}}.bin`

- Genereer een HTML flamegraph:

`memray flamegraph {{pad/naar/bestand}}.bin`
