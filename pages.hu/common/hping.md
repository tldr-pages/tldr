# hping

> Parancssor-orientált TCP/IP csomag-összeszerelő és -elemző. A `ping` parancs ihlette. További információ: <http://www.hping.org>.

- A localhost pingelése TCP-n keresztül:

`hping3 {{localhost}}`

- Egy IP-cím TCP-n keresztüli pingelése egy adott porton:

`hping3 -p {{80}} -S {{192.168.1.1}}`

- IP-cím pingelése UDP-n keresztül a 80-as porton:

`hping3 --udp -p {{80}} -S {{192.168.1.1}}`

- TCP-portok egy adott IP-címen történő letapogatása:

`hping3 --scan {{80,3000,9000}} -S {{192.168.1.1}}`

- Töltési teszt elvégzése a 80-as porton:

`hping3 --flood -p {{80}} -S {{192.168.1.1}}`
