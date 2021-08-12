# badblocks

> Căutați un dispozitiv pentru blocuri necorespunzătoare.
> Unele utilizări ale blocurilor de badblocks pot provoca acțiuni distructive, cum ar fi ștergerea tuturor datelor de pe un disc, inclusiv tabela de partiții.
> Mai multe informaţii: <https://manned.org/badblocks>

- Căutați un disc pentru blocuri necorespunzătoare utilizând un test non-distructiv doar în citire:

`sudo badblocks {{/dev/sdX}}`

- Căutați un disc nemontat pentru blocuri necorespunzătoare cu un test nedistructiv de citire-scriere:

`sudo badblocks -n {{/dev/sdX}}`

- Căutați un disc nemontat pentru blocuri proaste cu un test de scriere distructiv:

`sudo badblocks -w {{/dev/sdX}}`

- Căutați un disc nemontat pentru blocuri proaste cu un test de scriere distructiv și arătați starea verbose:

`sudo badblocks -svw {{/dev/sdX}}`

- Căutați un disc nemontat în modul distructiv și ieșiți blocuri găsite într-un fișier:

`sudo badblocks -o {{path/to/file}} -w {{/dev/sdX}}`

- Căutați un disc nemontat în modul distructiv cu viteză îmbunătățită utilizând dimensiunea blocului 4K și numărul de blocuri 64K:

`sudo badblocks -w -b {{4096}} -c {{65536}} {{/dev/sdX}}`
