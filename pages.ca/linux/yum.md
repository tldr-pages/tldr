# yum

> Administrador de paquets per RHEL, CentOS i Fedora (per versions anteriors).
> Més informació: <https://manned.org/yum>.

- Instal·la un nuevo paquete:

`yum install {{paquet}}`

- Instal·la un nou paquet responent si a totes les preguntes (també funciona amb actualitzacions, útil per actualitzacions automàtiques):

`yum -y install {{paquet}}`

- Troba quin paquet proveeix un arxiu determinat:

`yum provides {{comandament}}`

- Elimina un paquet:

`yum remove {{paquet}}`

- Mostra les actualitzacions disponibles per els paquets instal·lats:

`yum check-update`

- Actualitza els paquets instal·lats a les versions més recents disponibles:

`yum upgrade`
