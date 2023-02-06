# nmcli agent

> Futtassa az nmcli-t NetworkManager titkos ügynökként vagy polkit ügynökként. Ez az alparancs a `nmcli a` címmel is meghívható. További információ: <https://networkmanager.dev/docs/api/latest/nmcli.html>.

- Regisztrálja az nmcli-t titkos ügynökként, és figyeljen a titkos kérésekre:

`nmcli agent secret`

- Regisztrálja az nmcli-t polkit ügynökként, és figyeljen az engedélyezési kérésekre:

`nmcli agent polkit`

- Az nmcli titkos ügynökként és polkit ügynökként történő regisztrálása:

`nmcli agent all`
