# openttd

> A Microprose "Transport Tycoon Deluxe" című játék nyílt forráskódú klónja. További információ: <https://www.openttd.org>.

- Új játék indítása:

`openttd -g`

- A mentett játék betöltése az induláskor:

`openttd -g {{path/to/file}}`

- Indítás a megadott ablakfelbontással:

`openttd -r {{1920x1080}}`

- Egyéni konfigurációs fájlban való indítás:

`openttd -c {{path/to/file}}`

- Indítás a kiválasztott video-, hang- és zenei vezérlővel:

`openttd -v {{video_driver}} -s {{sound_driver}} -m {{music_driver}}`

- Dedikált szerver indítása, a háttérben forkolással:

`openttd -f -D {{host}}:{{port}}`

- Jelszóval csatlakozzon egy kiszolgálóhoz:

`openttd -n {{host}}:{{port}}#{{player_name}} -p {{password}}`
