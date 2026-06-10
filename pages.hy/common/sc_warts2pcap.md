# sc_warts2pcap

> Գրեք `.warts` ֆայլերում ներառված փաթեթները PCAP ֆայլում:.
> Սա հնարավոր է միայն `tbit`, `sting` կամ `sniff` տիպի փաթեթների համար:.
> Լրացուցիչ տեղեկություններ. <https://www.caida.org/catalog/software/scamper/>:.

- Փոխակերպեք մի քանի `.warts` ֆայլերի տվյալները մեկ PCAP ֆայլի.:

`sc_warts2pcap -o {{path/to/output.pcap}} {{path/to/file1.warts path/to/file2.warts ...}}`

- Տվյալները փոխարկեք `.warts` ֆայլից PCAP ֆայլի և փաթեթները դասակարգեք ըստ ժամանակի դրոշմակնիքի.:

`sc_warts2pcap -s -o {{path/to/output.pcap}} {{path/to/file.warts}}`
