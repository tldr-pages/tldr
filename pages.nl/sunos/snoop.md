# snoop

> Network packet sniffer.
> SunOS equivalent van tcpdump.
> Meer informatie: <https://www.unix.com/man-page/sunos/1m/snoop>.

- Capteer de pakketten van een specifieke netwerk interface:

`snoop -d {{e1000g0}}`

- Slaag de pakketten op in een bestand, in plaats van ze weer te geven:

`snoop -o {{bestandsnaam}}`

- Toon de verboze protocal layer samenvatting van de pakketten in een bestand:

`snoop -V -i {{bestandsnaam}}`

- Capteren van netwerk pakketten die van een bepaalde host komen en naar een gegeven poort gaan:

`snoop to port {{poort}} from host {{hostnaam}}`

- Capteren en weergave van een hex-dump van network pakketten die uitgewisseld zijn tussen twee IP addressen:

`snoop -x0 -p4 {{ip_adres_1}} {{ip_adres_2}}`
