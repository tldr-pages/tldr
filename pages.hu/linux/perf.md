# perf

> Linux teljesítménymérő mérések keretrendszere. További információ: <https://perf.wiki.kernel.org>.

- Egy parancs alapvető teljesítményszámláló statisztikáinak megjelenítése:

`perf stat {{gcc hello.c}}`

- Rendszer szintű valós idejű teljesítményszámláló profil megjelenítése:

`sudo perf top`

- Egy parancs futtatása és profiljának rögzítése a `perf.data` oldalon:

`sudo perf record {{command}}`

- Egy meglévő folyamat profiljának rögzítése a `perf.data`:

`sudo perf record -p {{pid}}`

- Olvassa be a `perf.data` címet (amelyet a `perf record` létrehozott) és jelenítse meg a profilt:

`sudo perf report`
