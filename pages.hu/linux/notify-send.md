# notify-send

> Az aktuális asztali környezet értesítési rendszerét használja értesítés létrehozására. További információ: <https://manned.org/notify-send>.

- Értesítés megjelenítése "Teszt" címmel és "Ez egy teszt" tartalommal:

`notify-send "{{Test}}" "{{This is a test}}"`

- Egyéni ikonnal ellátott értesítés megjelenítése:

`notify-send -i {{icon.png}} "{{Test}}" "{{This is a test}}"`

- Értesítés megjelenítése 5 másodpercig:

`notify-send -t 5000 "{{Test}}" "{{This is a test}}"`

- Értesítés megjelenítése egy alkalmazás ikonjával és nevével:

`notify-send "{{Test}}" --icon={{google-chrome}} --app-name="{{Google Chrome}}"`
