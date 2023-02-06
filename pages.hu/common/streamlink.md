# streamlink

> Kivonja a streameket a különböző szolgáltatásokból, és átvezeti őket a kívánt videólejátszóba. További információ: <https://streamlink.github.io>.

- Megkísérli a streamek kinyerését a megadott URL-címről, és ha sikerül, kiírja a rendelkezésre álló streamek listáját, amelyek közül választhat:

`streamlink {{example.com/stream}}`

- Megnyit egy streamet a megadott minőségben:

`streamlink {{example.com/stream}} {{720p60}}`

- Válassza ki az elérhető legmagasabb vagy legalacsonyabb minőséget:

`streamlink {{example.com/stream}} {{best|worst}}`

- Annak megadása, hogy melyik lejátszót használja a stream-adatok betáplálására (alapértelmezés szerint a VLC-t használja, ha talál):

`streamlink --player={{mpv}} {{example.com/stream}} {{best}}`

- Adja meg, hogy mennyi időt ugorjon a stream elejétől. Élő adatfolyam esetén ez egy negatív eltolás a stream végétől (visszatekerés):

`streamlink --hls-start-offset {{[HH:]MM:SS}} {{example.com/stream}} {{best}}`

- Ugrás az élő adatfolyam elejére, vagy a lehető leghátrábbra:

`streamlink --hls-live-restart {{example.com/stream}} {{best}}`

- Lejátszás helyett a stream adatainak fájlba írása:

`streamlink --output {{path/to/file.ts}} {{example.com/stream}} {{best}}`

- Megnyitja a streamet a lejátszóban, ugyanakkor egy fájlba írja azt:

`streamlink --record {{path/to/file.ts}} {{example.com/stream}} {{best}}`
