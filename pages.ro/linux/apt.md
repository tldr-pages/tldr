# apt

> Utilitar de gestionare a pachetelor pentru distribuțiile bazate pe Debian.
> Înlocuire recomandată pentru apt-get atunci când este utilizat interactiv în versiunile Ubuntu 16.04 și ulterioare.
> Mai multe informaţii: <https://manpages.debian.org/latest/apt/apt.8.html>

- Actualizați lista de pachete și versiuni disponibile (este recomandat să rulați acest lucru înainte de alte comenzi `apt`):

`sudo apt update`

- Caută un pachet dat:

`apt search {{package}}`

- Afișați informații pentru un pachet:

`apt show {{package}}`

- Instalați un pachet sau actualizați-l la cea mai recentă versiune disponibilă:

`sudo apt install {{package}}`

- Eliminați un pachet (folosind `purge` în schimb, de asemenea, elimină fișierele sale de configurare):

`sudo apt remove {{package}}`

- Upgrade toate pachetele instalate la cele mai noi versiuni disponibile:

`sudo apt upgrade`

- Listează toate pachetele:

`apt list`

- Lista pachetelor instalate:

`apt list --installed`
