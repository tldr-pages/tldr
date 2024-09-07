# iwlist

> Get detailed information from a wireless interface.
> More information: <https://manned.org/iwlist.8>.

- Display the list of access points and ad-hoc cells in range:

`iwlist {{wireless_interface}} scan`

- Display available frequencies in the device:

`iwlist {{wireless_interface}} frequency`

- List the bit-rates supported by the device:

`iwlist {{wireless_interface}} rate`

- List the WPA authentication parameters currently set:

`iwlist {{wireless_interface}} auth`

- List all the WPA encryption keys set in the device:

`iwlist {{wireless_interface}} wpakeys`

- List the encryption key sizes supported and list all the encryption keys set in the device:

`iwlist {{wireless_interface}} keys`

- List the various power management attributes and modes of the device:

`iwlist {{wireless_interface}} power`

- List generic information elements set in the device (used for WPA support):

`iwlist {{wireless_interface}} genie`
