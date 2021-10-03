# raw

> Bind a Unix raw character device.
> More information: <https://manned.org/raw.8>.

- Bind a raw character device to a block device:

`raw /dev/raw/raw{{1}} {{/dev/block_device}}`

- Query an existing binding instead of setting a new one:

`raw /dev/raw/raw{{1}}`

- Query all bound raw devices:

`raw -qa`
