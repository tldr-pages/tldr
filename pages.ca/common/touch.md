# touch

> Canvia els temps d'accés i modificació d'un fitxer (atime, ntime).
> Més informació: <https://manned.org/man/freebsd-13.1/touch>.

- Crea un o múltiples fitxers o canvia els temps al temps actual:

`touch {{camí/al/fitxer}}`

- Estableix el temps d'un fitxer a una data i hora específica:

`touch -t {{YYYYMMDDHHMM.SS}} {{camí/al/fitxer}}`

- Estableix el temps en un fitxer a fa una hora:

`touch -d "{{-1 hour}}" {{camí/al/fitxer}}`

- Fa servir el temps d'un fitxer per establir el temps d'un segons fitxer:

`touch -r {{camí/al/fitxer1}} {{camí/al/fitxer2}}`

- Crea múltiples fitxers:

`touch {{camí/al/fitxer{1,2,3}.txt}}`
