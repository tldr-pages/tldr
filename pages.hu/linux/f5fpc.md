# f5fpc

> A BIG-IP Edge saját fejlesztésű kereskedelmi SSL VPN kliense. További információ: <https://techdocs.f5.com/kb/en-us/products/big-ip_apm/manuals/product/apm-client-configuration-11-4-0/4.html>.

- Nyisson új VPN-kapcsolatot:

`sudo f5fpc --start`

- Új VPN-kapcsolat megnyitása egy adott állomáshoz:

`sudo f5fpc --start --host {{host.example.com}}`

- Adjon meg egy felhasználónevet (a felhasználónak jelszót kell megadnia):

`sudo f5fpc --start --host {{host.example.com}} --username {{user}}`

- Az aktuális VPN-állapot megjelenítése:

`sudo f5fpc --info`

- A VPN-kapcsolat leállítása:

`sudo f5fpc --stop`
