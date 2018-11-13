# zramctl

> Setup and control zram devices.
> Use `mke2fs` or `mkswap` to format zram devices to partitions.

- Check if zram is enabled:

`lsmod | grep -i zram`

- Enable zram with 2 devices (use `zramctl` to configure the devices further):

`sudo modprobe zram num_devices={{2}}`

- Find and initialise the next free zram device to a 2GB virtual drive using LZ4 compression:

`sudo zramctl --find --size {{2GB}} --algorithm {{lz4}}`

- List currently initialised devices:

`zramctl`
