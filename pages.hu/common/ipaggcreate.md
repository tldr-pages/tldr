# ipaggcreate

> Összesített statisztikák készítése a TCP/IP-dumpokról. További információ: <https://manned.org/ipaggcreate>.

- Megszámolja a pcap-fájlban megjelenő egyes forráscímekről küldött csomagok számát:

`ipaggcreate --src {{path/to/file.pcap}}`

- A hálózati interfészről beolvasott csomagok csoportosítása és számolása IP-csomaghossz szerint:

`ipaggcreate --interface {{eth0}} --length`

- A pcap-fájlban megjelenő egyes címpárok között küldött bájtok számának megszámlálása:

`ipaggcreate --address-pairs --bytes {{path/to/file.pcap}}`
