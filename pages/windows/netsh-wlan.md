# netsh wlan

> Manage wireless networks.
> More information: <https://www.serverwatch.com/guides/netsh-commands/>.

- Show all available wireless networks:

`netsh wlan show networks`

- Connect to a wireless network with a specific SSID:

`netsh wlan connect name={{SSID}}`

- Disconnect from the current wireless network:

`netsh wlan disconnect`

- Show current wireless network interfaces and status:

`netsh wlan show interfaces`

- Export a wireless network profile to an XML file:

`netsh wlan export profile name={{SSID}} folder={{C:\path\to\folder}} key=clear`

- Delete a saved wireless network profile:

`netsh wlan delete profile name={{SSID}}`

- Enable hosted network (turn PC into Wi-Fi hotspot):

`netsh wlan set hostednetwork mode=allow ssid={{SSID}} key={{password}}`

- Start the hosted network:

`netsh wlan start hostednetwork`
