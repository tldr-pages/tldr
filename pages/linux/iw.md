# iw

> Show and manipulate wireless devices.
> See also: `iw dev`, `nmcli`, `iwctl`.
> More information: <https://wireless.docs.kernel.org/en/latest/en/users/documentation/iw.html>.

- Scan for available wireless networks:

`iw dev {{wlanX}} scan`

- Join an open wireless network:

`iw dev {{wlanX}} connect {{SSID}}`

- Close the current connection:

`iw dev {{wlanX}} disconnect`

- Show information about the current connection:

`iw dev {{wlanX}} link`

- List all physical and logical wireless network interfaces:

`iw dev`

- List all wireless capabilities for all physical hardware interfaces:

`iw phy`

- List the kernel's current wireless regulatory domain information:

`iw reg get`

- Display help:

`iw help`
