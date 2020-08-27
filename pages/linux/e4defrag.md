# e4defrag

> Defragment an ext4 file system.

- Defragment the file system:

`e4defrag {{/dev/sdXN}}`

- See how fragmented a file system is:

`e4defrag -c {{/dev/sdXN}}`

- Print errors and the fragmentation count before and after each file:

`e4defrag -v {{/dev/sdXN}}`
