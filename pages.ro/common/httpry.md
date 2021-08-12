# httpry

> Un sniffer ușor de pachete pentru afișarea și înregistrarea traficului HTTP.
> Poate fi rulat în timp real afișarea traficului pe măsură ce este analizată sau ca un proces daemon care se conectează la un fișier de ieșire.
> Mai multe informaţii: <http://dumpsterventures.com/jason/httpry/>

- Salvați ieșirea într-un fișier:

`httpry -o {{path/to/file.log}}`

- Ascultați pe o interfață specifică și salvați ieșirea într-un fișier binar format pcap:

`httpry {{eth0}} -b {{path/to/file.pcap}}`

- Filtrați ieșirea printr-o listă separată prin virgulă de verbe HTTP:

`httpry -m {{get|post|put|head|options|delete|trace|connect|patch}}`

- Citiți dintr-un fișier de captare de intrare și filtrați prin IP:

`httpry -r {{path/to/file.log}} '{{host 192.168.5.25}}'`

- Rulați ca proces daemon:

`httpry -d -o {{path/to/file.log}}`
