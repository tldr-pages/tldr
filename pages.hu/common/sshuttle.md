# sshuttle

> Átlátszó proxy-kiszolgáló, amely SSH-kapcsolaton keresztül csatornázza a forgalmat. Nem igényel root jogot vagy bármilyen speciális beállítást a távoli SSH-kiszolgálón, bár a helyi gépen root hozzáférést kér. További információ: <https://manned.org/sshuttle>.

- Az összes IPv4 TCP-forgalom továbbítása egy távoli SSH-kiszolgálón keresztül:

`sshuttle --remote={{username}}@{{sshserver}} {{0.0.0.0/0}}`

- Az összes DNS-forgalom továbbítása a kiszolgáló alapértelmezett DNS-feloldójára is:

`sshuttle --dns --remote={{username}}@{{sshserver}} {{0.0.0.0/0}}`

- Minden forgalom továbbítása, kivéve az adott alhálózathoz kötött forgalmat:

`sshuttle --remote={{username}}@{{sshserver}} {{0.0.0.0/0}} --exclude {{192.168.0.1/24}}`

- A tproxy módszerrel minden IPv4 és IPv6 forgalmat továbbíthat:

`sshuttle --method=tproxy --remote={{username}}@{{sshserver}} {{0.0.0.0/0}} {{::/0}} --exclude={{your_local_ip_address}} --exclude={{ssh_server_ip_address}}`
