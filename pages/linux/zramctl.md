# zramctl

> Setup and control zram devices

- Check if zram is enabled:

`lsmod | grep -i zram`

- Enable zram with 2 devices:

`sudo modprobe zram num_devices={{2}}`

- Initialise the next free zram device to a 2GB virtual drive:

`sudo zramctl --find --streams {{compression_streams_count}} --size {{2GB}} --algorithm lz4`

- List currently initialised devices:

`zramctl`

- Format a zram device to ext4:

`sudo mkfs.ext4 {{/dev/zram0}}`
