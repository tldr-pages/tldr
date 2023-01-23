# podman build

> Démon nélküli eszköz konténerképek készítésére. A Podman Docker-CLI-vel összehasonlítható parancssoros eszközt biztosít. Egyszerűen fogalmazva: `alias docker=podman`. További információ: <https://docs.podman.io/en/latest/markdown/podman-build.1.html>.

- Készítsen egy képet a `Dockerfile` vagy a `Containerfile` segítségével a megadott könyvtárban:

`podman build {{path/to/directory}}`

- Kép létrehozása egy megadott címkével:

`podman build --tag {{image_name:version}} {{path/to/directory}}`

- Kép létrehozása nem szabványos fájlból:

`podman build --file {{Containerfile.different}} .`

- Kép létrehozása anélkül, hogy korábban gyorsítótárazott képeket használna:

`podman build --no-cache {{path/to/directory}}`

- Kép létrehozása minden kimenet elfojtásával:

`podman build --quiet {{path/to/directory}}`
