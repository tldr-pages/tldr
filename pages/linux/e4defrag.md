# e4defrag

> Defragment an ext4 filesystem.

- Defragment the filesystem:

`e4defrag {{/dev/sdXN}}`

- See how fragmented a filesystem is:

`e4defrag -c {{/dev/sdXN}}`

- Print errors and the fragmentation count before and after each file:

`e4defrag -v {{/dev/sdXN}}`
