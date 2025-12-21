# zoneadm

> Administrează zonele Oracle Solaris.
> Mai multe informații: <https://docs.oracle.com/cd/E88353_01/html/E72487/zoneadm-8.html>.

- Listează toate zonele și starea lor curentă:

`zoneadm list -cv`

- Verifică configurarea unei zone specifice:

`sudo zoneadm -z {{nume_zonă}} verify`

- Instalează o zonă:

`sudo zoneadm -z {{nume_zonă}} install`

- Pornește o zonă:

`sudo zoneadm -z {{nume_zonă}} boot`

- Repornește o zonă:

`sudo zoneadm -z {{nume_zonă}} reboot`

- Oprește o zonă, ocolind orice scripturi de închidere din interiorul zonei:

`sudo zoneadm -z {{nume_zonă}} halt`

- Dezinstalează o zonă:

`sudo zoneadm -z {{nume_zonă}} uninstall`
