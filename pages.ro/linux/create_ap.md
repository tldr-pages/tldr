# create_ap

> Creați un AP (punct de acces) pe orice canal.
> Mai multe informaţii: <https://github.com/oblique/create_ap>

- Creați o rețea deschisă fără fraze de acces:

`create_ap {{wlan0}} {{eth0}} {{access_point_ssid}}`

- Utilizați o frază de acces WPA + WPA2:

`create_ap {{wlan0}} {{eth0}} {{access_point_ssid}} {{passphrase}}`

- Creați un punct de acces fără partajarea Internetului:

`create_ap -n {{wlan0}} {{acces_point_ssid}} {{passphrase}}`

- Creați o rețea de legătură cu partajarea Internetului:

`create_ap -m bridge {{wlan0}} {{eth0}} {{access_point_ssid}} {{passphrase}}`

- Creați o rețea de legătură cu partajarea Internetului și o interfață de pod pre-configurată:

`create_ap -m bridge {{wlan0}} {{br0}} {{access_point_ssid}} {{passphrase}}`

- Creați un port de acces pentru partajarea Internetului din aceeași interfață WiFi:

`create_ap {{wlan0}} {{wlan0}} {{access_point_ssid}} {{passphrase}}`

- Alegeți un alt driver de adaptor WiFi:

`create_ap --driver {{wifi_adapter}} {{wlan0}} {{eth0}} {{access_point_ssid}} {{passphrase}}`
