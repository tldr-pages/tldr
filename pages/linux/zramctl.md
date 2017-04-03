# zramctl

> Setup and control zram devices.

- Check if zram is enabled:

`lsmod | grep -i zram`

- Enable zram with 2 devices:

`sudo modprobe zram num_devices={{2}}`

- Find and initialise the next free zram device to a 2GB virtual drive using lz4 compression:

`sudo zramctl --find --size {{2GB}} --algorithm {{lz4}}`

- List currently initialised devices:

`zramctl`
