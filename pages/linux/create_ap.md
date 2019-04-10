# create_ap

> Create an AP (Access Point) at any channel. 
> For installation instructions refer  [official documentation](https://github.com/oblique/create_ap).

- No passphrase (open network):

`create_ap wlan0 eth0 MyAccessPoint`

- For an example, I have internet access on my eth0 network, and my wireless interface is wlan0, I want the name of my network to be “ubuntuGuide” and the password as “12345678” so:

`create_ap eth0 wlan0 ubuntuGuide 12345678`

- WPA + WPA2 passphrase:

`create_ap wlan0 eth0 MyAccessPoint MyPassPhrase`

- AP without Internet sharing:

`create_ap -n wlan0 MyAccessPoint MyPassPhrase`

- Bridged Internet sharing:

`create_ap -m bridge wlan0 eth0 MyAccessPoint MyPassPhrase`

- Bridged Internet sharing (pre-configured bridge interface):

`create_ap -m bridge wlan0 br0 MyAccessPoint MyPassPhrase`

- Internet sharing from the same WiFi interface:

`create_ap wlan0 wlan0 MyAccessPoint MyPassPhrase`

- Choose a different WiFi adapter driver:

`create_ap --driver rtl871xdrv wlan0 eth0 MyAccessPoint MyPassPhrase`
