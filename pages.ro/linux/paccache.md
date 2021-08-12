# paccache

> Un utilitar de curăţare cache-ului pacman.

- Elimină toate versiunile de pachete, dar cele mai recente 3 din memoria cache pacman:

`paccache -r`

- Setați numărul de versiuni de pachete pentru a păstra:

`paccache -rk {{num_versions}}`

- Efectuați o alergare uscată și afișați numărul de pachete candidate pentru ștergere:

`paccache -d`

- Mutați pachetele candidate într-un director în loc să le ștergeți:

`paccache -m {{path/to/directory}}`
