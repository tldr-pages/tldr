# netsh wlan

> Manage wireless networks on Windows using the command line.
> More information: <https://docs.microsoft.com/en-us/windows-server/networking/technologies/netsh/netsh-wlan>.

- Show all available wireless networks:

`netsh wlan show networks`

- Connect to a wireless network with a specific SSID:

`netsh wlan connect name="{{SSID}}"`

- Disconnect from the current wireless network:

`netsh wlan disconnect`

- Show the current wireless network profile:

`netsh wlan show interfaces`

- Export a wireless network profile to an XML file:

`netsh wlan export profile name="{{SSID}}" folder="{{C:\path\to\folder}}" key=clear`

- Delete a saved wireless network profile:

`netsh wlan delete profile name="{{SSID}}"`

- Add a new wireless network profile from an XML file:

`netsh wlan add profile filename="{{profile.xml}}"`

- Enable hosted network (turn PC into Wi-Fi hotspot):

`netsh wlan set hostednetwork mode=allow ssid="{{SSID}}" key="{{password}}"`

- Start the hosted network:

`netsh wlan start hostednetwork`

- Stop the hosted network:

`netsh wlan stop hostednetwork`
