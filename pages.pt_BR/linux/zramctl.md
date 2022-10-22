# zramctl

> Configura e controla dispositivos zram.
> Use `mkfs` ou `mkswap` para formatar dispositivos zram para partições.
> Mais informações: <https://manned.org/zramctl>.

- Verifica se o zram está habilitado:

`lsmod | grep -i zram`

- Habilita o zram com um número dinâmico de dispositivos (use `zramctl` para configurar ainda mais os dispositivos):

`sudo modprobe zram`

- Habilita o zram com exatamente 2 dispositivos:

`sudo modprobe zram num_devices={{2}}`

- Encontra e inicializa o próximo dispositivo zram gratuito em uma unidade virtual de 2 GB usando a compressão LZ4:

`sudo zramctl --find --size {{2GB}} --algorithm {{lz4}}`

- Lista dispositivos atualmente inicializados:

`zramctl`
