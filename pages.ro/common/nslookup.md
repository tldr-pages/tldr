# nslookup

> Server de nume de interogare pentru diferite înregistrări de domeniu.

- Interogați serverul de nume implicit al sistemului dvs. pentru o adresă IP (O înregistrare) a domeniului:

`nslookup {{example.com}}`

- Interogare un server de nume dat pentru o înregistrare NS a domeniului:

`nslookup -type=NS {{example.com}} {{8.8.8.8}}`

- Interogare pentru o căutare inversă (înregistrare PTR) a unei adrese IP:

`nslookup -type=PTR {{54.240.162.118}}`

- Interogare pentru orice înregistrări disponibile utilizând protocolul TCP:

`nslookup -vc -type=ANY {{example.com}} `

- Interogare un server de nume dat pentru întregul fișier zonă (transfer de zonă) a domeniului utilizând protocolul TCP:

`nslookup -vc -type=AXFR {{example.com}} {{name_server}}`

- Interogare pentru un server de e-mail (înregistrare MX) a domeniului, care afișează detaliile tranzacției:

`nslookup -type=MX -debug {{example.com}}`

- Interogarea unui server de nume dat pe un anumit număr de port pentru o înregistrare TXT a domeniului:

`nslookup -port={{port_number}} -type=TXT {{example.com}} {{name_server}}`
