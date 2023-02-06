# tmux

> Terminál multiplexer. Több munkamenetet tesz lehetővé ablakokkal, ablakpanelekkel és egyebekkel. Lásd még: `zellij` és `screen`. További információ: <https://github.com/tmux/tmux>.

- Új munkamenet indítása:

`tmux`

- Új, megnevezett munkamenet indítása:

`tmux new -s {{name}}`

- Meglévő munkamenetek listázása:

`tmux ls`

- Csatlakozás a legutóbb használt munkamenethez:

`tmux attach`

- Leválás az aktuális munkamenetről (tmux munkameneten belül):

`Ctrl-B d`

- Új ablak létrehozása (tmux munkameneten belül):

`Ctrl-B c`

- Váltás munkamenetek és ablakok között (tmux munkameneten belül):

`Ctrl-B w`

- Munkamenet megszakítása név szerint:

`tmux kill-session -t {{name}}`
