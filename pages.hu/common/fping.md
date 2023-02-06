# fping

> Erőteljesebb ping, amely több állomás pingelésére is képes. További információ: <https://fping.org>.

- Egy alhálózaton belüli élő hosztok listája, amelyet egy hálózati maszkból generáltak:

`fping -a -g 192.168.1.0/24`

- Egy IP-tartományból generált alhálózaton belüli élő hosztok listája:

`fping -a -g 192.168.1.1 192.168.1.254`

- Nem elérhető hosztok listája egy alhálózaton belül, amelyet egy hálózati maszkból generáltak:

`fping -u -g 192.168.1.0/24`
