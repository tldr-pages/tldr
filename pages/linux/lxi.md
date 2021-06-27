# lxi

> Tool for controling LXI compatible instruments such as oscilloscopes.
> More information: <https://github.com/lxi-tools/lxi-tools>.

- Discover LXI devices on available networks:

`lxi discover`

- Capture a screenshot using plugin autodetection:

`lxi screenshot --address {{10.42.1.20}}`

- Capture a screenshot using specifying a plugin:

`lxi screenshot --address {{10.42.1.20}} --plugin {{rigol-1000z}}`

- Send SCPI command to an instrument:

`lxi scpi --address {{10.42.1.20}} {{"*IDN?"}}`

- Run a benchmark for request and response performance:

`lxi benchmark --address {{10.42.1.20}}`
