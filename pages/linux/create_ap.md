# create_ap

> Create an AP (Access Point) at any channel.
> More information: <https://github.com/oblique/create_ap>.

- Create an open network with no passphrase:

`create_ap {{wlan0}} {{eth0}} {{access_point_ssid}}`

- Use a WPA + WPA2 passphrase:

`create_ap {{wlan0}} {{eth0}} {{access_point_ssid}} {{passphrase}}`

- Create an access point without Internet sharing:

`create_ap -n {{wlan0}} {{access_point_ssid}} {{passphrase}}`

- Create a bridged network with Internet sharing:

`create_ap -m bridge {{wlan0}} {{eth0}} {{access_point_ssid}} {{passphrase}}`

- Create a bridged network with Internet sharing and a pre-configured bridge interface:

`create_ap -m bridge {{wlan0}} {{br0}} {{access_point_ssid}} {{passphrase}}`

- Create an access port for Internet sharing from the same Wi-Fi interface:

`create_ap {{wlan0}} {{wlan0}} {{access_point_ssid}} {{passphrase}}`

- Choose a different Wi-Fi adapter driver:

`create_ap --driver {{wifi_adapter}} {{wlan0}} {{eth0}} {{access_point_ssid}} {{passphrase}}`
