# e4defrag

> Egy ext4 fájlrendszer defragmentálása. További információ: <https://manned.org/e4defrag>.

- Defragmentálja a fájlrendszert:

`e4defrag {{/dev/sdXN}}`

- Nézze meg, mennyire töredezett a fájlrendszer:

`e4defrag -c {{/dev/sdXN}}`

- Nyomtassa ki a hibákat és a töredezettségi számot minden fájl előtt és után:

`e4defrag -v {{/dev/sdXN}}`
