# jhsdb

> Csatlakozzon egy Java-folyamathoz, vagy indítson el egy postmortem hibakeresőt, hogy elemezze a lezuhant Java Virtual Machine magdömpingjét. További információ: <https://manned.org/jhsdb>.

- Egy Java-folyamat verem- és zárinformációinak nyomtatása:

`jhsdb jstack --pid {{pid}}`

- Magdömping megnyitása interaktív hibakeresési módban:

`jhsdb clhsdb --core {{path/to/core_dump}} --exe {{path/to/jdk/bin/java}}`

- Távoli hibakeresési kiszolgáló indítása:

`jhsdb debugd --pid {{pid}} --serverid {{optional_unique_id}}`

- Csatlakozás egy folyamathoz interaktív hibakeresési módban:

`jhsdb clhsdb --pid {{pid}}`
