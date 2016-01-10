# wpa_cli

> Add and configure wlan interfaces.

- Scan for available networks:

`wpa_cli scan`
`wpa_cli scan_results`

- Add a network:

`wpa_cli add_network {{number}}`

- Configure the network, e.g. set SSID and passkey:

`wpa_cli set_network {{number}} ssid {{SSID}}`
`wpa_cli set_network {{number}} psk {{passkey}}`

- Enable network:

`wpa_cli enable_network {{number}}`

- Save config:

`wpa_cli save_config`
