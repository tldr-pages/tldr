# dnsmasq

> Server DNS, DHCP, TFTP e PXE leggero.
> Maggiori informazioni: <https://manned.org/dnsmasq>.

- Avvia dnsmasq con configurazione predefinita:

`dnsmasq`

- Esegui dnsmasq in primo piano (per debug):

`dnsmasq --no-daemon`

- Specifica un file di configurazione personalizzato:

`dnsmasq --conf-file={{percorso/del/config.conf}}`

- Abilita logging verboso:

`dnsmasq --log-queries --log-facility=-`

- Imposta un intervallo DHCP e durata lease:

`dnsmasq --dhcp-range={{192.168.0.50,192.168.0.150,12h}}`

- Visualizza versione:

`dnsmasq --version`
