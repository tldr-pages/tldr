# iw dev

> Show and manipulate wireless devices.
> For a list of channels, frequencies, and reg information: <https://wireless.docs.kernel.org/en/latest/en/developers/documentation/channellist.html>.
> More information: <https://wireless.docs.kernel.org/en/latest/en/users/documentation/iw.html>.

- Set device to monitor mode (interface must be down first. See also: `ip link`):

`sudo iw dev {{wlanX}} set type monitor`

- Set device to managed mode (interface must be down first):

`sudo iw dev {{wlanX}} set type managed`

- Set device Wi-Fi channel (device must first be in monitor mode with the interface up):

`sudo iw dev {{wlanX}} set channel {{channel_number}}`

- Set device Wi-Fi frequency in Mhz (device must first be in monitor mode with the interface up):

`sudo iw dev {{wlanX}} set freq {{freq_in_mhz}}`

- Show all known station info:

`iw dev {{wlanX}} station dump`

- Create a virtual interface in monitor mode with a specific MAC address:

`sudo iw dev {{wlanX}} interface add "{{vif_name}}" type monitor addr {{12:34:56:aa:bb:cc}}`

- Delete virtual interface:

`sudo iw dev "{{vif_name}}" del`
