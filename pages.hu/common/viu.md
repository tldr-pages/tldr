# viu

> Egy kis parancssori alkalmazás képek megtekintésére a terminálból. További információ: <https://github.com/atanunq/viu>.

- Kép vagy animált GIF megjelenítése:

`viu {{path/to/file}}`

- Kép vagy GIF renderelése az internetről a `curl` segítségével:

`curl -s {{https://example.com/image.png}} | viu -`

- Kép renderelése átlátszó háttérrel:

`viu -t {{path/to/file}}`

- Egy kép renderelése egy adott szélességű és magasságú képponttal:

`viu -w {{width}} -h {{height}} {{path/to/file}}`

- Kép vagy GIF kép renderelése és fájlnevének megjelenítése:

`viu -n {{path/to/file}}`
