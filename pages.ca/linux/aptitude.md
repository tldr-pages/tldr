# aptitude

> Eina de gestió de paquets per a Debian i Ubuntu.
> Més informació: <https://manned.org/aptitude>.

- Sincronitza la llista de paquets i versions disponibles (es recomana executar aquest commandament abans que qualsevol altre `aptitude`):

`sudo aptitude update`

- Instal·lar un nou paquet i les seves dependències:

`sudo aptitude install {{paquet}}`

- Buscar un paquet:

`aptitude search {{paquet}}`

- Cercar un paquet instal·lat (`?installed` es un terme de cerca de `aptitude`):

`aptitude search '?installed({{paquet}})'`

- Elimina un paquet i tots els paquets que depenen d'ell:

`sudo aptitude remove {{paquet}}`

- Actualitza tots els paquets a les noves versions disponibles:

`sudo aptitude upgrade`

- Actualitza paquets instal·lats (com `aptitude upgrade`), però elimina els paquets obsolets i instal·la paquets nous per satisfer les dependències:

`sudo aptitude full-upgrade`

- Manté un paquet perquè no sigui actualitzat automàticament:

`sudo aptitude hold '?installed({{paquete}})'`
