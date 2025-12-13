# zoneadm

> Administer Oracle Solaris zones.
> See also: `zonecfg`, `zlogin`.
> More information: <https://manned.org/zoneadm.8>.

- List all zones and their current status:

`zoneadm list -cv`

- Verify the configuration of a specific zone:

`zoneadm -z {{zone_name}} verify`

- Install a zone:

`zoneadm -z {{zone_name}} install`

- Boot (start) a zone:

`zoneadm -z {{zone_name}} boot`

- Reboot a zone:

`zoneadm -z {{zone_name}} reboot`

- Halt (stop) a zone:

`zoneadm -z {{zone_name}} halt`

- Uninstall a zone:

`zoneadm -z {{zone_name}} uninstall`
