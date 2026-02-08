# ps

> Informationen über laufende Prozesse.
> Weitere Informationen: <https://manned.org/ps>.

- Liste alle laufenden Prozesse auf:

`ps aux`

- Liste alle laufenden Prozesse einschließlich des vollständigen Kommandostrings:

`ps auxww`

- Suche nach einem Prozess, der einem String entspricht (die Klammern verhindern, dass `grep` sich selbst findet):

`ps aux | grep {{[s]tring}}`

- Liste alle Prozesse des aktuellen Benutzers im vollständigen Format:

`ps {{[-u|--user]}} $(id {{[-u|--user]}}) -F`

- Liste alle Prozesse des aktuellen Benutzers als Baumstruktur:

`ps {{[-u|--user]}} $(id {{[-u|--user]}}) f`

- Ermittle die übergeordnete PID eines Prozesses:

`ps {{[-o|--format]}} ppid= {{[-p|--pid]}} {{pid}}`

- Sortiere Prozesse nach Speicherverbrauch:

`ps --sort size`
