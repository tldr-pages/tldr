# openfortivpn

> VPN kliens a Fortinet saját PPP+SSL VPN megoldásához. További információ: <https://github.com/adrienverge/openfortivpn>.

- Csatlakozás egy VPN-hez felhasználónévvel és jelszóval:

`openfortivpn --username={{username}} --password={{password}}`

- Csatlakozás egy VPN-hez egy adott konfigurációs fájl segítségével (alapértelmezett beállítás: `/etc/openfortivpn/config`):

`sudo openfortivpn --config={{path/to/config}}`

- Csatlakozás egy VPN-hez az állomás és a port megadásával:

`openfortivpn {{host}}:{{port}}`

- Megbízhat egy adott átjáróban a tanúsítványa sha256-os összegének átadásával:

`openfortivpn --trusted-cert={{sha256_sum}}`
