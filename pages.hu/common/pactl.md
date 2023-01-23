# pactl

> Egy futó PulseAudio hangkiszolgáló vezérlése. További információ: <https://manned.org/pactl>.

- Listázza ki az összes sinket (vagy más típusokat - a sinkek kimenetek, a sink-bemenetek pedig aktív hangfolyamokat jelentenek):

`pactl list {{sinks}} short`

- Módosítsa az alapértelmezett sink (kimenet) értékét 1-re (a számot a `list` alparanccsal lehet lekérdezni):

`pactl set-default-sink {{1}}`

- A 627-es sink-bemenet áthelyezése az 1-es sinkbe:

`pactl move-sink-input {{627}} {{1}}`

- Állítsa az 1. nyelő hangerejét 75%-ra:

`pactl set-sink-volume {{1}} {{0.75}}`

- Kapcsolja be a némítást az alapértelmezett nyelőn (a `@DEFAULT_SINK@` speciális névvel):

`pactl set-sink-mute {{@DEFAULT_SINK@}} toggle`
