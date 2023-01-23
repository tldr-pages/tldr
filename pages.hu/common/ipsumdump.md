# ipsumdump

> Összefoglalja a TCP/IP-dumpokat emberi és gépi olvasásra alkalmas ASCII formátumba. További információ: <https://manned.org/ipsumdump>.

- A pcap fájlban lévő összes csomag forrás és cél IP-címének kiírása:

`ipsumdump --src --dst {{path/to/file.pcap}}`

- Egy adott hálózati interfészről beolvasott összes csomag időbélyegének, forráscímének, forrásportjának, célcímének, célportjának és protokolljának nyomtatása:

`ipsumdump --interface {{eth0}} -tsSdDp`

- A pcap-fájlban lévő összes csomag anonimizált forráscímének, anonimizált célcímének és IP-csomaghosszának nyomtatása:

`ipsumdump --src --dst --length --anonymize {{path/to/file.pcap}}`
