# nmcli device

> Hardvereszköz-kezelés a NetworkManagerrel. Ez az alparancs a `nmcli d` címmel is meghívható. További információ: <https://networkmanager.dev/docs/api/latest/nmcli.html>.

- Az összes hálózati interfész állapotának kiírása:

`nmcli device status`

- Az elérhető Wi-Fi hozzáférési pontok kinyomtatása:

`nmcli device wifi`

- Csatlakozás a Wi-Fi hálózathoz egy megadott névvel és jelszóval:

`nmcli device wifi connect {{ssid}} password {{password}}`

- Jelszó és QR-kód nyomtatása az aktuális Wi-Fi hálózathoz:

`nmcli device wifi show-password`
