# perf

> Cadru pentru măsurătorile contorului de performanță Linux.

- Afișează statistici contor de performanță de bază pentru o comandă:

`perf stat {{gcc hello.c}}`

- Afișează profilul contorului de performanță la nivel de sistem în timp real:

`sudo perf top`

- Rulați o comandă și înregistrați profilul său în `perf.data`:

`sudo perf record {{command}}`

- Citiți `perf.data` (creat de `perf record`) și afișați profilul:

`sudo perf report`
