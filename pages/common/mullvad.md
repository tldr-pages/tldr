# mullvad

> CLI client for Mullvad VPN.
> See also: `fastd`, `ivpn`, `mozillavpn`, `warp-cli`.
> More information: <https://mullvad.net/en/help/how-use-mullvad-cli>.

- Link your Mullvad account with the specified account number:

`mullvad account set {{account_number}}`

- Enable LAN access while VPN is on:

`mullvad lan set allow`

- Select a server in a specific city:

`mullvad relay set location {{se}} {{mma}}`

- Select a specific server:

`mullvad relay set location {{se-mma-wg-001}}`

- Establish the VPN tunnel:

`mullvad connect`

- Check status of VPN tunnel:

`mullvad status`

- Check the account expiration date and obtain the device name:

`mullvad account get`
