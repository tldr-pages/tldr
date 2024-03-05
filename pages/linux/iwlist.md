# iwlist

> Get more detailed wireless information from a wireless wireless_interface.
> More information: <https://manned.org/iwlist.8>.

- Give the list of Access Points and Ad-Hoc cells in range:

`iwlist {{wireless_interface}} scan`

- Give the list of available frequencies in the device:

`iwlist {{wireless_interface}} frequency`

- List the bit-rates supported by the device:

`iwlist {{wireless_interface}} rate`

- List the WPA authentication parametes curently set:

`iwlist {{wireless_interface}} auth`

- List all the WPA encryption keys set in the device:

`iwlist {{wireless_interface}} wpakeys`

- List the encryption key sizes supported and list all the encryption keys set in the device:

`iwlist {{wireless_interface}} keys`

- List the various power management attributes and modes of the device:

`iwlist {{wireless_interface}} power`

- List the Generic Information Elements set in the device (used for WPA support):

`iwlist {{wireless_interface}} genie`
