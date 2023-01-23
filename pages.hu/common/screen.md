# screen

> Egy munkamenet nyitva tartása egy távoli kiszolgálón. Több ablak kezelése egyetlen SSH-kapcsolattal. Lásd még: `tmux` és `zellij`. További információ: <https://manned.org/screen>.

- Új képernyős munkamenet indítása:

`screen`

- Új, megnevezett képernyő munkamenet indítása:

`screen -S {{session_name}}`

- Új démon indítása és a kimenet naplózása a `screenlog.x` címen:

`screen -dmLS {{session_name}} {{command}}`

- Megnyílt képernyő munkamenetek megjelenítése:

`screen -ls`

- Újracsatlakozás egy nyitott képernyőhöz:

`screen -r {{session_name}}`

- Leválás egy képernyőn belülről:

`Ctrl + A, D`

- Az aktuális képernyő munkamenet megszakítása:

`Ctrl + A, K`

- Leválasztott képernyő megszakítása:

`screen -X -S {{session_name}} quit`
