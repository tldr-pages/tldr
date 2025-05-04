# mullvad

> CLI client for Mullvad VPN.
> See also: `fastd`, `ivpn`, `mozillavpn`, `warp-cli`.
> More information: <https://mullvad.net/>.

- Link your Mullvad account with the specified account number:

`mullvad account set {{account_number}}`

- Enable LAN access while VPN is on:

`mullvad lan set allow`

- Establish the VPN tunnel:

`mullvad connect`

- Check status of VPN tunnel:

`mullvad status`

- Check expire date of account and obtain device name:

`mullvad account get`
