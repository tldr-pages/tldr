# protonvpn-cli

> A ProtonVPN szolgáltatás hivatalos kliense a parancssorból. További információk: <https://github.com/ProtonVPN/linux-cli>.

- Jelentkezzen be a ProtonVPN fiókjába:

`protonvpn-cli login {{username}}`

- Indítson el egy kill switchet a ProtonVPN-hez való csatlakozáskor:

`protonvpn-cli killswitch --on`

- Csatlakozzon a ProtonVPN-hez interaktívan:

`protonvpn-cli connect`

- A kapcsolat állapotának megjelenítése:

`protonvpn-cli status`

- Rosszindulatú programok blokkolása a ProtonVPN NetShield használatával:

`protonvpn-cli netshield --malware`

- A ProtonVPN-hez való csatlakozás megszakítása:

`protonvpn-cli disconnect`

- A ProtonVPN aktuális konfigurációjának megjelenítése:

`protonvpn-cli config --list`

- Súgó megjelenítése egy alparancshoz:

`protonvpn-cli {{subcommand}} --help`
