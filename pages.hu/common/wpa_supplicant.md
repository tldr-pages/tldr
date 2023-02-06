# wpa_supplicant

> Védett vezeték nélküli hálózatok kezelése. További információ: <https://manned.org/wpa_supplicant.1>.

- Csatlakozás védett vezeték nélküli hálózathoz:

`wpa_supplicant -i {{interface}} -c {{path/to/wpa_supplicant_conf.conf}}`

- Csatlakozzon egy védett vezeték nélküli hálózathoz, és futtassa azt egy démonban:

`wpa_supplicant -B -i {{interface}} -c {{path/to/wpa_supplicant_conf.conf}}`
