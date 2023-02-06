# create_ap

> Hozzon létre egy AP-t (hozzáférési pontot) bármely csatornán. További információ: <https://github.com/oblique/create_ap>.

- Hozzon létre egy nyílt hálózatot jelszó nélkül:

`create_ap {{wlan0}} {{eth0}} {{access_point_ssid}}`

- Használjon WPA + WPA2 jelszót:

`create_ap {{wlan0}} {{eth0}} {{access_point_ssid}} {{passphrase}}`

- Hozzáférési pont létrehozása internetmegosztás nélkül:

`create_ap -n {{wlan0}} {{access_point_ssid}} {{passphrase}}`

- Hozzon létre áthidalt hálózatot internetmegosztással:

`create_ap -m bridge {{wlan0}} {{eth0}} {{access_point_ssid}} {{passphrase}}`

- Hídhálózat létrehozása internetmegosztással és előre konfigurált hídinterfésszel:

`create_ap -m bridge {{wlan0}} {{br0}} {{access_point_ssid}} {{passphrase}}`

- Hozzáférési port létrehozása internetmegosztáshoz ugyanarról a Wi-Fi interfészről:

`create_ap {{wlan0}} {{wlan0}} {{access_point_ssid}} {{passphrase}}`

- Válasszon másik Wi-Fi adapter illesztőprogramot:

`create_ap --driver {{wifi_adapter}} {{wlan0}} {{eth0}} {{access_point_ssid}} {{passphrase}}`
