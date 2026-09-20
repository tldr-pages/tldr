# snoop

> Netwerk pakket sniffer.
> SunOS equivalent van `tcpdump`.
> Meer informatie: <https://www.unix.com/man-page/sunos/1m/snoop>.

- Leg de pakketten van een specifieke netwerkinterface vast:

`snoop -d {{e1000g0}}`

- Sla de pakketten op in een bestand, in plaats van ze weer te geven:

`snoop -o {{bestandsnaam}}`

- Toon de verbose protocol layer samenvatting van de pakketten in een bestand:

`snoop -V -i {{bestandsnaam}}`

- Leg netwerkpakketten vast die van een bepaalde host komen en naar een gegeven poort gaan:

`snoop to port {{poort}} from host {{hostnaam}}`

- Leg een hex-dump vast van netwerkpakketten die uitgewisseld zijn tussen twee IP-adressen en toon deze:

`snoop -x0 -p4 {{ip_adres_1}} {{ip_adres_2}}`
