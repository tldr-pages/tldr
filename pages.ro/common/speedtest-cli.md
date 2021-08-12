# speedtest-cli

> Interfață de linie de comandă neoficială pentru testarea lățimii de bandă pe internet utilizând https://speedtest.net.
> A se vedea, de asemenea, „test de viteză” pentru CLI oficial.
> Mai multe informaţii: <https://github.com/sivel/speedtest-cli>

- Rulați un test de viteză:

`speedtest-cli`

- Rulați un test de viteză și afișați valorile în octeți, în loc de biți:

`speedtest-cli --bytes`

- Rulați un test de viteză folosind `HTTPS`, în loc de `HTTP`:

`speedtest-cli --secure`

- Rulați un test de viteză fără a efectua teste de descărcare:

`speedtest-cli --no-download`

- Rulați un test de viteză și generați o imagine a rezultatelor:

`speedtest-cli --share`

- Listează toate serverele `speedtest.net, sortate după distanță:

`speedtest-cli --list`

- Rulați un test de viteză pe un anumit server speedtest.net:

`speedtest-cli --server {{server_id}}`

- Rulați un test de viteză și afișați rezultatele ca JSON (suprimă informațiile de progres):

`speedtest-cli --json`
