# wpa_supplicant

> Manage protected wireless networks.
> More information: <https://manned.org/wpa_supplicant.1>.

- Join a protected wireless network:

`wpa_supplicant -i {{interface}} -c {{path/to/wpa_supplicant_conf.conf}}`

- Join a protected wireless network and run it in a daemon:

`wpa_supplicant -B -i {{interface}} -c {{path/to/wpa_supplicant_conf.conf}}`
