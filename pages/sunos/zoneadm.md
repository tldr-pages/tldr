# zoneadm

> Administer Oracle Solaris zones.
> More information: <https://docs.oracle.com/cd/E88353_01/html/E72487/zoneadm-8.html>.

- List all zones and their current status:

`zoneadm list -cv`

- Verify the configuration of a specific zone:

`sudo zoneadm -z {{zone_name}} verify`

- Install a zone:

`sudo zoneadm -z {{zone_name}} install`

- Boot (start) a zone:

`sudo zoneadm -z {{zone_name}} boot`

- Reboot a zone:

`sudo zoneadm -z {{zone_name}} reboot`

- Halt (stop) a zone, bypassing any shutdown scripts inside the zone:

`sudo zoneadm -z {{zone_name}} halt`

- Uninstall a zone:

`sudo zoneadm -z {{zone_name}} uninstall`
