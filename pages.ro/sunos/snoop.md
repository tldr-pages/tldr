# snoop

> Analizator de pachete de rețea.
> Echivalentul SunOS pentru tcpdump.
> Mai multe informații: <https://www.unix.com/man-page/sunos/1m/snoop>.

- Capturează pachete pe o interfață de rețea specifică:

`snoop -d {{e1000g0}}`

- Salvează pachetele capturate într-un fișier în loc să le afișeze:

`snoop -o {{cale/către/fișier}}`

- Afișează un rezumat detaliat al stratului de protocol al pachetelor dintr-un fișier:

`snoop -V -i {{cale/către/fișier}}`

- Capturează pachete de rețea care provin de la un nume de gazdă și se îndreaptă către un anumit port:

`snoop to port {{port}} from host {{nume_gazdă}}`

- Capturează și afișează un hex-dump al pachetelor de rețea schimbate între două adrese IP:

`snoop -x0 -p4 {{ip1}} {{ip2}}`