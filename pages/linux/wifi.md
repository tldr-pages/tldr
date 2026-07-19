# wifi

> Enable, disable, and reconfigure wireless radios on OpenWrt.
> More information: <https://openwrt.org/docs/guide-user/network/wifi/basic>.

- Bring up all wireless devices (default action):

`wifi`

- Bring up a specific radio device:

`wifi up {{radio0}}`

- Shut down all wireless devices:

`wifi down`

- Shut down a specific radio device:

`wifi down {{radio0}}`

- Reload wireless configuration without a full network restart:

`wifi reload`

- Reconfigure wireless after editing `/etc/config/wireless`:

`wifi reconf`

- Show wireless status:

`wifi status`

- Detect hardware and write a default wireless config:

`wifi config`
