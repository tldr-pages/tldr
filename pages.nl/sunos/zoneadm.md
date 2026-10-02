# zoneadm

> Beheer Oracle Solaris zones.
> Meer informatie: <https://docs.oracle.com/cd/E88353_01/html/E72487/zoneadm-8.html>.

- Toon alle zones en hun huidige status:

`zoneadm list -cv`

- Verifieer de configuratie van een specifieke zone:

`sudo zoneadm -z {{zone_naam}} verify`

- Installeer een zone:

`sudo zoneadm -z {{zone_naam}} install`

- Boot (start) een zone:

`sudo zoneadm -z {{zone_naam}} boot`

- Herstart een zone:

`sudo zoneadm -z {{zone_naam}} reboot`

- Stop een zone, waarbij eventuele afsluitscripts binnen de zone worden overgeslagen:

`sudo zoneadm -z {{zone_naam}} halt`

- Verwijder de installatie van een zone:

`sudo zoneadm -z {{zone_naam}} uninstall`
