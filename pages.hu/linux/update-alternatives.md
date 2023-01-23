# update-alternatives

> Kényelmes eszköz szimbolikus linkek karbantartására az alapértelmezett parancsok meghatározásához. További információ: <https://manned.org/update-alternatives>.

- Szimbolikus hivatkozás hozzáadása:

`sudo update-alternatives --install {{path/to/symlink}} {{command_name}} {{path/to/command_binary}} {{priority}}`

- Szimbolikus link beállítása a `java` számára:

`sudo update-alternatives --config {{java}}`

- Szimbolikus hivatkozás eltávolítása:

`sudo update-alternatives --remove {{java}} {{/opt/java/jdk1.8.0_102/bin/java}}`

- Megadott parancsra vonatkozó információk megjelenítése:

`update-alternatives --display {{java}}`

- Az összes parancs és az aktuális kiválasztásuk megjelenítése:

`update-alternatives --get-selections`
