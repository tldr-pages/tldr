# wpa_cli

> add and configure wlan interfaces

- scan for available networks

`wpa_cli scan`
`wpa_cli scan_results`

- add a network

`wpa_cli add_network {{number}}`

- configure the network, e.g. set SSID and passkey

`wpa_cli set_network {{number}} ssid {{SSID}}`
`wpa_cli set_network {{number}} psk {{passkey}}`

- enable network

`wpa_cli enable_network {{number}}`

- save config

`wpa_cli save_config`
