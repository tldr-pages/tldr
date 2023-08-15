# Kismet

> A wireless network and device detector, sniffer, wardriving tool, and WIDS (wireless intrusion detection) framework.
> Kismet needs to be run with root privileges.
> More information: <https://www.kismetwireless.net/>.

- Capture packets from a specific wireless interface:

`kismet -c {{wlan0}}`

- Monitor multiple channels on a wireless interface:

`kismet -c {{wlan0,wlan1}} -m`

- Capture packets and save them to a specific directory:

`kismet -c {{wlan0}} -d /path/to/output`

- Start Kismet with a specific configuration file: 

`kismet -c {{wlan0}} -f /path/to/config.conf`

- Monitor and log data to a SQLite database:

`kismet -c {{wlan0}} --log-to-db`

- Monitor using a specific data source (e.g., rtl433):

`kismet -c {{wlan0}} --data-source=rtl433`

- Enable alerts for specific events (e.g., new APs):

`kismet -c {{wlan0}} --enable-alert=new_ap`

- Display detailed information about a specific AP's packets:

`kismet -c {{wlan0}} --info {{BSSID}}`

