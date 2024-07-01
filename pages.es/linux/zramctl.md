# zramctl

> Configura y controla dispositivos zram.
> Usa `mkfs` o `mkswap` para formatear dispositivos zram a particiones.
> Más información: <https://manned.org/zramctl>.

- Comprueba si zram está habilitado:

`lsmod | grep -i zram`

- Habilita zram con un número dinámico de dispositivos (usa `zramctl` para configurar más dispositivos):

`sudo modprobe zram`

- Habilita zram con exactamente 2 dispositivos:

`sudo modprobe zram num_devices={{2}}`

- Encuentra e inicializa el siguiente dispositivo zram libre a una unidad virtual de 2 GB usando compresión LZ4:

`sudo zramctl --find --size {{2GB}} --algorithm {{lz4}}`

- Lista los dispositivos actualmente inicializados:

`sudo zramctl`
