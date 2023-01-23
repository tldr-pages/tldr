# openconnect

> VPN-kliens a Cisco AnyConnect VPN-ekhez és másokhoz. További információ: <https://www.infradead.org/openconnect/manual.html>.

- Csatlakozás egy kiszolgálóhoz:

`openconnect {{vpn.example.org}}`

- Csatlakozás egy kiszolgálóhoz, elágazás a háttérben:

`openconnect --background {{vpn.example.org}}`

- A háttérben futó kapcsolat megszüntetése:

`killall -SIGINT openconnect`

- Csatlakozás egy kiszolgálóhoz, beállítások beolvasása egy konfigurációs fájlból:

`openconnect --config={{path/to/file}} {{vpn.example.org}}`

- Csatlakozás egy kiszolgálóhoz és hitelesítés egy adott SSL-ügyféltanúsítvánnyal:

`openconnect --certificate={{path/to/file}} {{vpn.example.org}}`
