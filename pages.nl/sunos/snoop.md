# snoop

> Network packet sniffer.
> SunOS equivalent van tcpdump.
> Meer informatie: <https://www.unix.com/man-page/sunos/1m/snoop>.

- Bekijk de paketten van een specifieke netwerk interface:

`snoop -d {{e1000g0}}`

- Slaag de paketten op in een bestand, in plaats van ze weer te geven:

`snoop -o {{filename}}`

- Toon de verboze protocal layer samenvatting van de paketten in een bestand:

`snoop -V -i {{filename}}`

- Capteren van netwerk paketten die van een bepaalde host komen en naar een gegeven poort gaan:

`snoop to port {{port}} from host {{hostname}}`

- Capteren en weergave van een hex-dump van network packetten die uitgewisseld zijn tussen twee IP addressen:

`snoop -x0 -p4 {{ip_address_1}} {{ip_address_2}}`
