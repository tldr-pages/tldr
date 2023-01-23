# zramctl

> A zram eszközök beállítása és vezérlése. A `mkfs` vagy a `mkswap` segítségével a zram eszközöket partíciókká formázhatja. További információ: <https://manned.org/zramctl>.

- Ellenőrizze, hogy a zram engedélyezve van-e:

`lsmod | grep -i zram`

- Engedélyezze a zramot dinamikus eszközszámmal (az eszközök további konfigurálásához használja a `zramctl` címet):

`sudo modprobe zram`

- Engedélyezze a zramot pontosan 2 eszközzel:

`sudo modprobe zram num_devices={{2}}`

- Keresse meg és inicializálja a következő szabad zram eszközt egy 2 GB-os virtuális meghajtóvá LZ4 tömörítéssel:

`sudo zramctl --find --size {{2GB}} --algorithm {{lz4}}`

- A jelenleg inicializált eszközök listája:

`zramctl`
