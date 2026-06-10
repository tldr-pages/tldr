# ipaggcreate

> Կազմել TCP/IP աղբավայրերի համախառն վիճակագրություն:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/ipaggcreate>:.

- Հաշվեք PCAP ֆայլում հայտնված յուրաքանչյուր աղբյուրի հասցեից ուղարկված փաթեթների քանակը.:

`ipaggcreate --src {{path/to/file.pcap}}`

- Խմբավորել և հաշվել ցանցային ինտերֆեյսից կարդացվող փաթեթներն ըստ IP փաթեթի երկարության.:

`ipaggcreate --interface {{eth0}} --length`

- Հաշվեք PCAP ֆայլում հայտնված յուրաքանչյուր հասցեային զույգի միջև ուղարկված բայթերի քանակը.:

`ipaggcreate --address-pairs --bytes {{path/to/file.pcap}}`
