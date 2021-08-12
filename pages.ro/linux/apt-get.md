# apt-get

> Utilitar de gestionare a pachetelor Debian și Ubuntu.
> Căutați pachete utilizând `apt-cache`.
> Mai multe informaţii: <https://manpages.debian.org/latest/apt/apt-get.8.html>

- Actualizați lista de pachete și versiuni disponibile (este recomandat să rulați acest lucru înainte de alte comenzi `apt-get`):

`apt-get update`

- Instalați un pachet sau actualizați-l la cea mai recentă versiune disponibilă:

`apt-get install {{package}}`

- Elimină un pachet:

`apt-get remove {{package}}`

- Eliminați un pachet și fișierele sale de configurare:

`apt-get purge {{package}}`

- Upgrade toate pachetele instalate la cele mai noi versiuni disponibile:

`apt-get upgrade`

- Curățați depozitul local - eliminând fișierele pachetelor (`.deb`) din descărcările întrerupte care nu mai pot fi descărcate:

`apt-get autoclean`

- Eliminați toate pachetele care nu mai sunt necesare:

`apt-get autoremove`

- Upgrade-ul pachetelor instalate (cum ar fi `upgrade`), dar elimina pachetele învechite si instaleaza pachete suplimentare pentru a satisface noi dependențe:

`apt-get dist-upgrade`
