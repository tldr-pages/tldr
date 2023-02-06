# history

> Parancssori előzmények. További információ: <https://www.gnu.org/software/bash/manual/html_node/Bash-History-Builtins.html>.

- A parancsok előzménylistájának megjelenítése a sorszámokkal:

`history`

- Az utolsó 20 parancs megjelenítése (a `zsh` oldalon a 20. parancstól kezdve az összes parancsot megjeleníti):

`history {{20}}`

- A parancsok előzménylistájának törlése (csak az aktuális `bash` shell esetében):

`history -c`

- Az előzményfájl felülírása az aktuális `bash` shell előzményeivel (gyakran a `history -c` parancssorral kombinálva az előzmények törléséhez):

`history -w`

- A megadott eltolásnál lévő előzménybejegyzés törlése:

`history -d {{offset}}`
