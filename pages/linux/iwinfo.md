# iwinfo

> Retrieve information about wireless interfaces on OpenWrt.
> More information: <https://openwrt.org/docs/guide-developer/ubus/iwinfo>.

- List all available wireless interfaces:

`iwinfo`

- Display detailed information on a specific wireless interface:

`iwinfo {{interface}} info`

- Scan for nearby wireless networks visible to the interface:

`iwinfo {{interface}} scan`

- List connected devices:

`iwinfo {{interface}} assoclist`

- List channels supported by the interface:

`iwinfo {{interface}} freqlist`

- List available transmit power levels for the interface:

`iwinfo {{interface}} txpowerlist`

- Display help:

`iwinfo h`
