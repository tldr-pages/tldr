# networksetup

> Configuration tool for Network System Preferences.
> More information: <https://support.apple.com/guide/remote-desktop/about-networksetup-apdd0c5a2d5/mac>.

- List available network service providers (Ethernet, Wi-Fi, Bluetooth, etc):

`networksetup -listallnetworkservices`

- Show network settings for a particular networking device:

`networksetup -getinfo "{{Wi-Fi}}"`

- Get currently connected Wi-Fi network name (Wi-Fi device usually en0 or en1):

`networksetup -getairportnetwork {{en0}}`

- Connect to a particular Wi-Fi network:

`networksetup -setairportnetwork {{en0}} {{Airport Network SSID}} {{password}}`
