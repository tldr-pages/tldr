# tcpdump

> Dump trafic într-o rețea.
> Mai multe informaţii: <https://www.tcpdump.org>

- Lista interfețelor de rețea disponibile:

`tcpdump -D`

- Capturați traficul unei interfețe specifice:

`tcpdump -i {{eth0}}`

- Capturează tot traficul TCP care arată conținutul (ASCII) în consola:

`tcpdump -A tcp`

- Capturează traficul de la sau către o gazdă:

`tcpdump host {{www.example.com}}`

- Capturarea traficului dintr-o interfață specifică, sursă, destinație și destinație port:

`tcpdump -i {{eth0}} src {{192.168.1.1}} and dst {{192.168.1.2}} and dst port {{80}}`

- Capturează traficul unei rețele:

`tcpdump net {{192.168.1.0/24}}`

- Captura tot traficul, cu excepția traficului peste portul 22 și de a salva într-un fișier imagine de memorie:

`tcpdump -w {{dumpfile.pcap}} port not {{22}}`

- Citiți dintr-un fișier imagine de memorie dat:

`tcpdump -r {{dumpfile.pcap}}`
