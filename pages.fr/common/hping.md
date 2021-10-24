# hping

> Outil en ligne de commande permettant d'assembler ou analyser des paquets TCP/IP.
> Inspirer par la commande `ping`.
> Plus d'informations : <http://www.hping.org>.

- Ping localhost via TCP :

`hping3 {{localhost}}`

- Ping une adresse IP, via TCP, sur un port spécifique :

`hping3 -p {{80}} -S {{192.168.1.1}}`

- Ping une adresse IP, via UDP, sur le port 80 :

`hping3 --udp -p {{80}} -S {{192.168.1.1}}`

- Scanner un ensemble de ports TCP, sur une adresse IP spécifique :

`hping3 --scan {{80,3000,9000}} -S {{192.168.1.1}}`

- Effectuer un test de montée en charge sur le port 80 :

`hping3 --flood -p {{80}} -S {{192.168.1.1}}`
