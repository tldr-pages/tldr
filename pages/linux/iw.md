# iw

> Show and manipulate wireless devices.
> See also: `iw dev`.
> More information: <https://wireless.docs.kernel.org/en/latest/en/users/documentation/iw.html>.

- Scan for available wireless networks:

`iw dev {{wlp}} scan`

- Join an open wireless network:

`iw dev {{wlp}} connect {{SSID}}`

- Close the current connection:

`iw dev {{wlp}} disconnect`

- Show information about the current connection:

`iw dev {{wlp}} link`

- List all physical and logical wireless network interfaces:

`iw dev`

- List all wireless capabilities for all physical hardware interfaces:

`iw phy`

- List the kernel's current wireless regulatory domain information:

`iw reg get`

- Display help for all commands:

`iw help`
