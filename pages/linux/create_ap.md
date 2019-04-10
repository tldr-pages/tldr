# create_ap

> Create an AP (Access Point) at any channel.

- Create an open network with no passphrase:

`create_ap {{wlan0}} {{eth0}} {{MyAccessPoint}}`

- Use a WPA + WPA2 passphrase:

`create_ap {{wlan0}} {{eth0}} {{MyAccessPoint}} {{MyPassPhrase}}`

- Create an access point without Internet sharing:

`create_ap -n {{wlan0}} {{MyAccessPoint}} {{MyPassPhrase}}`

- Create a bridged network with Internet sharing:

`create_ap -m bridge {{wlan0}} {{eth0}} {{MyAccessPoint}} {{MyPassPhrase}}`

- Create a bridged network with Internet sharing and a pre-configured bridge interface:

`create_ap -m bridge {{wlan0}} {{br0}} {{MyAccessPoint}} {{MyPassPhrase}}`

- Create an access port for Internet sharing from the same WiFi interface:

`create_ap {{wlan0}} {{wlan0}} {{MyAccessPoint}} {{MyPassPhrase}}`

- Choose a different WiFi adapter driver:

`create_ap --driver {{WifiAdapter}} {{wlan0}} {{eth0}} {{MyAccessPoint}} {{MyPassPhrase}}`
