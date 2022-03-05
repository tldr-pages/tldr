# wpa_cli

> Add and configure wlan interfaces.
> More information: <https://manned.org/wpa_cli>.

- Scan for available networks:

`wpa_cli scan`

- Show scan results:

`wpa_cli scan_results`

- Add a network:

`wpa_cli add_network {{number}}`

- Set a network's SSID:

`wpa_cli set_network {{number}} ssid "{{SSID}}"`

- Enable network:

`wpa_cli enable_network {{number}}`

- Save config:

`wpa_cli save_config`
