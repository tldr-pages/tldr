# protonvpn-cli connect

> Hivatalos kliens a ProtonVPN-hez való csatlakozáshoz a parancssorból. További információ: <https://protonvpn.com/support/linux-vpn-setup/>.

- Csatlakozás a ProtonVPN-hez interaktívan:

`protonvpn-cli connect`

- Csatlakozzon a ProtonVPN-hez a leggyorsabb elérhető szerverrel:

`protonvpn-cli connect --fastest`

- Csatlakozás a ProtonVPN-hez egy adott kiszolgálóval és egy adott protokollal:

`protonvpn-cli connect {{server_name}} --protocol {{udp|tcp}}`

- Csatlakozás a ProtonVPN-hez egy véletlenszerű szerverrel és egy adott protokollal:

`protonvpn-cli connect --random --protocol {{udp|tcp}}`

- Csatlakozás a ProtonVPN-hez a leggyorsabb Tor-támogató szerver használatával:

`protonvpn-cli connect --tor`

- Súgó megjelenítése:

`protonvpn-cli connect --help`
