# hping

> Linie de comandă orientată spre asamblor de pachete TCP/IP și analizor.
> Inspirat de comanda `ping`.
> Mai multe informaţii: <http://www.hping.org>

- Ping localhost peste TCP:

`hping3 {{localhost}}`

- Ping o adresă IP prin TCP pe un anumit port:

`hping3 -p {{80}} -S {{192.168.1.1}}`

- Ping o adresă IP peste UDP pe portul 80:

`hping3 --udp -p {{80}} -S {{192.168.1.1}}`

- Scanarea unui set de porturi TCP pe o anumită adresă IP:

`hping3 --scan {{80,3000,9000}} -S {{192.168.1.1}}`

- Efectuați un test de încărcare pe portul 80:

`hping3 --flood -p {{80}} -S {{192.168.1.1}}`
