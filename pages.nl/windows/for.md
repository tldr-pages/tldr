# for

> Voer conditioneel een commando meerdere keren uit.
> Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/for>.

- Voer de gegeven commando's uit voor de opgegeven set:

`for %{{variabele}} in ({{item_a item_b item_c}}) do ({{echo Loop wordt uitgevoerd}})`

- Itereer over een gegeven reeks nummers:

`for /l %{{variabele}} in ({{van}}, {{stap}}, {{tot}}) do ({{echo Loop wordt uitgevoerd}})`

- Itereer over een gegeven lijst van bestanden:

`for %{{variabele}} in ({{pad\naar\bestand1.ext pad\naar\bestand2.ext ...}}) do ({{echo Loop wordt uitgevoerd}})`

- Itereer over een gegeven lijst van mappen:

`for /d %{{variabele}} in ({{pad\naar\map1.ext pad\naar\map2.ext ...}}) do ({{echo Loop wordt uitgevoerd}})`

- Voer een gegeven commando uit in elke map:

`for /d %{{variabele}} in (*) do (if exist %{{variabele}} {{echo Loop wordt uitgevoerd}})`
