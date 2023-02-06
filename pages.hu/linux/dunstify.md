# dunstify

> Egy értesítési eszköz, amely az notify-send kiterjesztése, de több funkcióval rendelkezik, és a dunst köré épül. Minden olyan opcióval működik, ami az notify-send esetében is. További információ: <https://github.com/dunst-project/dunst/wiki/Guides>.

- Értesítés megjelenítése adott címmel és üzenettel:

`dunstify "{{Title}}" "{{Message}}"`

- Megadott sürgősségű értesítés megjelenítése:

`dunstify "{{Title}}" "{{Message}}" -u {{low|normal|critical}}`

- Üzenetazonosító megadása (felülírja az azonos azonosítóval rendelkező korábbi üzeneteket):

`dunstify "{{Title}}" "{{Message}}" -r {{123}}`

- A többi lehetséges opció megtekintéséhez:

`notify-send --help`
