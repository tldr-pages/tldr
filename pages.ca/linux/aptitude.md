# aptitude

> Eina de gestió de paquets per a Debian i Ubuntu.
> Més informació: <https://manpages.debian.org/latest/aptitude/aptitude.8.html>.

- Sincronitza la llista de paquets i versions disponibles (es recomana executar aquest commandament abans que qualsevol altre `aptitude`):

`aptitude update`

- Instal·lar un nou paquet i les seves dependències:

`aptitude install {{paquet}}`

- Buscar un paquet:

`aptitude search {{paquet}}`

- Cercar un paquet instal·lat (`?installed` es un terme de cerca de `aptitude`):

`aptitude search '?installed({{paquet}})'`

- Elimina un paquet i tots els paquets que depenen d'ell:

`aptitude remove {{paquet}}`

- Actualitza tots els paquets a les noves versions disponibles:

`aptitude upgrade`

- Actualitza paquets instal·lats (com `aptitude upgrade`), però elimina els paquets obsolets i instal·la paquets nous per satisfer les dependències:

`aptitude full-upgrade`

- Manté un paquet perquè no sigui actualitzat automàticament:

`aptitude hold '?installed({{paquete}})'`
