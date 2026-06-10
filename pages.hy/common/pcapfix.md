# pcapfix

> Վերանորոգեք վնասված կամ կոռումպացված PCAP և PcapNG ֆայլերը:.
> Լրացուցիչ տեղեկություններ. <https://f00l.de/pcapfix/>:.

- Վերանորոգեք PCAP/PCapNG ֆայլը (Նշում. PCAP ֆայլերի համար յուրաքանչյուր փաթեթի միայն առաջին 262144 բայթն է սկանավորվում):

`pcapfix {{path/to/file.pcapng}}`

- Վերանորոգեք ամբողջ PCAP ֆայլը.:

`pcapfix --deep-scan {{path/to/file.pcap}}`

- Վերանորոգեք PCAP/PcapNG ֆայլը և գրեք վերանորոգված ֆայլը նշված վայրում՝:

`pcapfix --outfile {{path/to/repaired.pcap}} {{path/to/file.pcap}}`

- Նշված ֆայլը վերաբերվեք որպես PcapNG ֆայլ՝ անտեսելով ավտոմատ ճանաչումը.:

`pcapfix --pcapng {{path/to/file.pcapng}}`

- Վերանորոգեք ֆայլը և մանրամասն ցուցադրեք գործընթացը.:

`pcapfix --verbose {{path/to/file.pcap}}`
