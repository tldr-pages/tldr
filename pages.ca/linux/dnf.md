# dnf

> Administrador de paquets per RHEL, CentOS i Fedora (Reemplaça a yum).
> Més informació: <https://dnf.readthedocs.io>.

- Actualitza tots els paquets a l'última versió disponible:

`sudo dnf update`

- Busca un paquet fent servir paraules clau:

`dnf search {{palabra_clau}}`

- Mostra informació sobre un paquet:

`dnf info {{paquet}}`

- Instal·la un nou paquet:

`sudo dnf install {{paquet}}`

- Instal·la un nou paquet responent si a totes les preguntes:

`sudo dnf install -y {{paquet}}`

- Desinstal·la un paquet:

`sudo dnf remove {{paquet}}`

- Llista tots els paquets instal·lats:

`dnf list --installed`

- Troba quin paquet proveeeix un arxiu determinat:

`dnf provides {{arxiu}}`
