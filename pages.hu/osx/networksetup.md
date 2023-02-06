# networksetup

> A hálózati rendszerbeállítások konfigurációs eszköze. További információ: <https://support.apple.com/guide/remote-desktop/about-networksetup-apdd0c5a2d5/mac>.

- Az elérhető hálózati szolgáltatók listája (Ethernet, Wi-Fi, Bluetooth stb.):

`networksetup -listallnetworkservices`

- Egy adott hálózati eszköz hálózati beállításainak megjelenítése:

`networksetup -getinfo "{{Wi-Fi}}"`

- Az aktuálisan csatlakoztatott Wi-Fi hálózat nevének lekérdezése (Wi-Fi eszköz általában en0 vagy en1):

`networksetup -getairportnetwork {{en0}}`

- Csatlakozás egy adott Wi-Fi hálózathoz:

`networksetup -setairportnetwork {{en0}} {{Airport Network SSID}} {{password}}`
