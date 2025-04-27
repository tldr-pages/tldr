# lxi

> Control LXI compatible instruments such as oscilloscopes.
> More information: <https://github.com/lxi-tools/lxi-tools#32-lxi>.

- Discover LXI devices on available networks:

`lxi discover`

- Capture a screenshot, detecting a plugin automatically:

`lxi screenshot {{[-a|--address]}} {{ip_address}}`

- Capture a screenshot using a specified plugin:

`lxi screenshot {{[-a|--address]}} {{ip_address}} {{[-p|--plugin]}} {{rigol-1000z}}`

- Send an SCPI command to an instrument:

`lxi scpi {{[-a|--address]}} {{ip_address}} "{{*IDN?}}"`

- Run a benchmark for request and response performance:

`lxi benchmark {{[-a|--address]}} {{ip_address}}`
