# synopkg

> Utilitar de gestionare a pachetelor pentru Synology DiskStation Manager.
> Mai multe informaţii: <https://www.synology.com/dsm>

- Listați numele pachetelor instalate:

`synopkg list --name`

- Lista pachetelor care depind de un anumit pachet:

`synopkg list --depend-on {{package}}`

- Start/Oprește un pachet:

`sudo synopkg {{start|stop}} {{package}}`

- Tipăriți starea unui pachet:

`synopkg status {{package}}`

- Dezinstalați un pachet:

`sudo synopkg uninstall {{package}}`

- Verificați dacă actualizările sunt disponibile pentru un pachet:

`synopkg checkupdate {{package}}`

- Upgrade toate pachetele la cea mai recentă versiune:

`sudo synopkg upgradeall`

- Instalați un pachet dintr-un fișier synopkg:

`sudo synopkg install {{path/to/package.spk}}`
