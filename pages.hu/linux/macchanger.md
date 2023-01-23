# macchanger

> Parancssori segédprogram a hálózati interfész MAC-címek manipulálására. További információ: <https://manned.org/macchanger>.

- Egy interfész aktuális és állandó MAC-címének megtekintése:

`macchanger --show {{interface}}`

- Az interfész beállítása véletlenszerű MAC-re:

`macchanger --random {{interface}}`

- Interfész beállítása egy adott MAC-re:

`macchanger --mac {{XX:XX:XX:XX:XX:XX}} {{interface}}`

- Az interfész visszaállítása az állandó hardver MAC-re:

`macchanger --permanent {{interface}}`
