# playerctl

> Segédprogram különböző médialejátszók vezérlésére. További információ: <https://github.com/altdesktop/playerctl>.

- Lejátszás átkapcsolása:

`playerctl play-pause`

- Következő média:

`playerctl next`

- Előző média:

`playerctl previous`

- Az összes lejátszó listája:

`playerctl --list-all`

- Parancs küldése egy adott lejátszónak:

`playerctl --player={{player_name}} {{command}}`

- Parancs küldése az összes játékosnak:

`playerctl --all-players {{command}}`

- Most lejátszás megjelenítése:

`playerctl metadata --format "Now playing: {{artist}} - {{album}} - {{title}}"`
