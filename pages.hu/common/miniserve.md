# miniserve

> Egyszerű HTTP fájlkiszolgáló CLI. További információ: <https://github.com/svenstaro/miniserve>.

- Egy könyvtár kiszolgálása:

`miniserve {{path/to/directory}}`

- Egyetlen fájl kiszolgálása:

`miniserve {{path/to/file}}`

- Egy könyvtár kiszolgálása HTTP alapszintű hitelesítéssel:

`miniserve --auth {{username}}:{{password}} {{path/to/directory}}`
