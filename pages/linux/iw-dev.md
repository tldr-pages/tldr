# iw dev

> Show and manipulate wireless devices.
> For a list of channels, frequencies and reg information: <https://wireless.docs.kernel.org/en/latest/en/developers/documentation/channellist.html>.
> More information: <https://wireless.docs.kernel.org/en/latest/en/users/documentation/iw.html>.

- Set device to monitor mode (interface must be down first. See also `ip link`):

`sudo iw dev {{wlp}} set type monitor`

- Set device to managed mode (interface must be down first):

`sudo iw dev {{wlp}} set type managed`

- Set device WiFi channel (device must first be in monitor mode with the interface up):

`sudo iw dev {{wlp}} set channel {{channel_number}}`

- Set device WiFi frequency in Mhz (device must first be in monitor mode with the interface up):

`sudo iw dev {{wlp}} set freq {{freq_in_mhz}}`

- Show all known station info:

`iw dev {{wlp}} station dump`

- Create a virtual interface in monitor mode with a specific MAC address:

`sudo iw dev {{wlp}} interface add "{{vif_name}}" type monitor addr {{12:34:56:aa:bb:cc}}`

- Delete virtual interface:

`sudo iw dev "{{vif_name}}" del`
