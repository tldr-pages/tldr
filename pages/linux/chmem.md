# chmem

> Modify the state of memory blocks (online or offline) in a Linux system.
> Typically used in virtualized environments to manage memory hotplug.
> More information: <https://manned.org/chmem>.

- Set a memory block offline:

`sudo chmem {{[-b|--block]}} {{[-d|--disable]}} {{block_number}}`

- Set a memory block online:

`sudo chmem {{[-b|--block]}} {{[-e|--enable]}} {{block_number}}`

- Set a memory range offline using hexadecimal addresses:

`sudo chmem {{[-d|--disable]}} 0x{{start_address}}-0x{{end_address}}`

- Set a memory range online using hexadecimal addresses:

`sudo chmem {{[-e|--enable]}} 0x{{start_address}}-0x{{end_address}}`

- Set memory online and assign it to a specific zone (e.g., Movable):

`sudo chmem {{[-e|--enable]}} 0x{{start_address}} {{[-z|--zone]}} {{Movable}}`

- Display help:

`chmem {{[-h|--help]}}`
