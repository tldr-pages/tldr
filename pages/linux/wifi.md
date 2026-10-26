# wifi

> Bring OpenWrt wireless devices up or down, and generate their configuration.
> With no arguments, this command brings wireless devices up.
> More information: <https://openwrt.org/docs/guide-user/network/wifi/basic>.

- Bring all wireless devices up:

`wifi`

- Bring all wireless devices down:

`wifi down`

- Bring one wireless device up:

`wifi up {{device}}`

- Reload the network configuration:

`wifi reload`

- Reconfigure wireless devices:

`wifi reconf`

- Detect radios and write `/etc/config/wireless` for devices that are not configured yet:

`wifi config`

- Show wireless status:

`wifi status`

- Check whether wireless devices are up (the exit status is non-zero when one is down):

`wifi isup`
