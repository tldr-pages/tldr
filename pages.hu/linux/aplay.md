# aplay

> Parancssori hanglejátszó az ALSA hangkártya-illesztőprogramhoz. További információ: <https://manned.org/aplay>.

- Egy adott fájl lejátszása (a mintavételi sebesség, bitmélység stb. automatikusan meghatározásra kerül a fájlformátumhoz):

`aplay {{path/to/file}}`

- Egy adott fájl első 10 másodpercének lejátszása 2500 Hz-en:

`aplay --duration={{10}} --rate={{2500}} {{path/to/file}}`

- A nyers fájl lejátszása 22050 Hz-es, mono, 8 bites, Mu-Law `.au` fájlként:

`aplay --channels={{1}} --file-type {{raw}} --rate={{22050}} --format={{mu_law}} {{path/to/file}}`
