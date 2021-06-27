# lxi

> Tool for controling LXI compatible instruments such as oscilloscopes.
> More information: <https://github.com/lxi-tools/lxi-tools>.

- Discover LXI devices on available networks:

`lxi discover`

- Capture a screenshot using plugin autodetection:

`lxi screenshot --address {{ip_adress}}`

- Capture a screenshot using specifying a plugin:

`lxi screenshot --address {{ip_adress}} --plugin {{rigol-1000z}}`

- Send an SCPI command to an instrument:

`lxi scpi --address {{ip_adress}} "{{*IDN?}}"`

- Run a benchmark for request and response performance:

`lxi benchmark --address {{ip_adress}}`
