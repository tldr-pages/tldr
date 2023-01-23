# openvpn

> OpenVPN kliens és démon bináris. További információ: <https://openvpn.net/>.

- Csatlakozás a kiszolgálóhoz egy konfigurációs fájl segítségével:

`sudo openvpn {{path/to/client.conf}}`

- Próbáljon meg egy nem biztonságos peer-to-peer alagutat létrehozni a bob.example.com állomáson:

`sudo openvpn --remote {{alice.example.com}} --dev {{tun1}} --ifconfig {{10.4.0.1}} {{10.4.0.2}}`

- Csatlakozás a várakozó bob.example.com állomáshoz titkosítás nélkül:

`sudo openvpn --remote {{bob.example.com}} --dev {{tun1}} --ifconfig {{10.4.0.2}} {{10.4.0.1}}`

- Kriptográfiai kulcs létrehozása és mentése fájlba:

`openvpn --genkey --secret {{path/to/key}}`

- Próbáljon meg statikus kulccsal peer-to-peer alagutat létrehozni a bob.example.com állomáson:

`sudo openvpn --remote {{alice.example.com}} --dev {{tun1}} --ifconfig {{10.4.0.1}} {{10.4.0.2}} --secret {{path/to/key}}`

- Csatlakozás a várakozó bob.example.com állomáshoz ugyanazzal a statikus kulccsal, mint a bob.example.com-on:

`sudo openvpn --remote {{bob.example.com}} --dev {{tun1}} --ifconfig {{10.4.0.2}} {{10.4.0.1}} --secret {{path/to/key}}`
