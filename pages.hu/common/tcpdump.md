# tcpdump

> A hálózaton zajló forgalom kiürítése. További információ: <https://www.tcpdump.org>.

- A rendelkezésre álló hálózati interfészek listázása:

`tcpdump -D`

- Egy adott interfész forgalmának rögzítése:

`tcpdump -i {{eth0}}`

- Az összes TCP-forgalom rögzítése, amely a konzol tartalmát mutatja (ASCII):

`tcpdump -A tcp`

- A forgalom rögzítése egy állomásról vagy egy állomás felé:

`tcpdump host {{www.example.com}}`

- Egy adott interfész, forrás, célállomás és célport forgalmának rögzítése:

`tcpdump -i {{eth0}} src {{192.168.1.1}} and dst {{192.168.1.2}} and dst port {{80}}`

- Egy hálózat forgalmának rögzítése:

`tcpdump net {{192.168.1.0/24}}`

- Az összes forgalom rögzítése, kivéve a 22-es porton keresztüli forgalmat, és mentés egy dump fájlba:

`tcpdump -w {{dumpfile.pcap}} port not {{22}}`

- Olvasás egy adott dump fájlból:

`tcpdump -r {{dumpfile.pcap}}`
