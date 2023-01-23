# chisel

> TCP-alagutak létrehozása. Tartalmazza a kliens és a szerver szolgáltatást is. További információ: <https://github.com/jpillora/chisel>.

- Chisel kiszolgáló futtatása:

`chisel server`

- Chisel-kiszolgáló futtatása egy adott porton:

`chisel server -p {{server_port}}`

- Futtasson olyan Chisel-kiszolgálót, amely felhasználónévvel és jelszóval hitelesített kapcsolatokat fogad:

`chisel server --auth {{username}}:{{password}}`

- Csatlakozás egy Chisel-kiszolgálóhoz és egy adott port alagútja egy távoli kiszolgálóhoz és porthoz:

`chisel client {{server_ip}}:{{server_port}} {{local_port}}:{{remote_server}}:{{remote_port}}`

- Csatlakozás egy Chisel-kiszolgálóhoz, és egy adott állomás és port alagútja egy távoli kiszolgálóhoz és porthoz:

`chisel client {{server_ip}}:{{server_port}} {{local_host}}:{{local_port}}:{{remote_server}}:{{remote_port}}`

- Csatlakozás egy Chisel-kiszolgálóhoz felhasználónév és jelszó hitelesítéssel:

`chisel client --auth {{username}}:{{password}} {{server_ip}}:{{server_port}} {{local_port}}:{{remote_server}}:{{remote_port}}`
