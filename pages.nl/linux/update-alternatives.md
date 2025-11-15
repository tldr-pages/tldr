# update-alternatives

> Een handig hulpmiddel voor het onderhouden van symbolische links om standaard commando's te bepalen.
> Meer informatie: <https://manned.org/update-alternatives>.

- Voeg een symbolische link toe:

`sudo update-alternatives --install {{pad/naar/symlink}} {{commando_naam}} {{pad/naar/commando_binary}} {{priority}}`

- Configureer een symbolische link voor `java`:

`sudo update-alternatives --config {{java}}`

- Verwijder een symbolische link:

`sudo update-alternatives --remove {{java}} {{/opt/java/jdk1.8.0_102/bin/java}}`

- Toon informatie over een specifiek commando:

`update-alternatives --display {{java}}`

- Toon alle commando's en hun huidige selectie:

`update-alternatives --get-selections`
