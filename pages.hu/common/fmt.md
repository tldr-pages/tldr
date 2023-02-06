# fmt

> Egy szöveges fájl átformázása a bekezdések összekapcsolásával és a sorszélesség adott karakterszámra (alapértelmezés szerint 75) való korlátozásával. További információ: <https://www.gnu.org/software/coreutils/fmt>.

- Egy fájl újraformázása:

`fmt {{path/to/file}}`

- Egy fájl átformázása, amely (legfeljebb) `n` karakterből álló kimeneti sorokat eredményez:

`fmt -w {{n}} {{path/to/file}}`

- Egy fájl újraformázása a megadott szélességnél rövidebb sorok összekapcsolása nélkül:

`fmt -s {{path/to/file}}`

- Egységes szóközzel (1 szóköz a szavak között és 2 szóköz a bekezdések között) átformázni egy fájlt:

`fmt -u {{path/to/file}}`
