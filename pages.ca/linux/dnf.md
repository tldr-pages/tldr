# dnf

> Administrador de paquets per RHEL, CentOS i Fedora (Reemplaça a yum).
> Més informació: <https://dnf.readthedocs.io>.

- Actualitza tots els paquets a l'última versió disponible:

`sudo dnf update`

- Busca un paquet fent servir paraules clau:

`dnf search {{palabra_clau1 palabra_clau2 ...}}`

- Mostra informació sobre un paquet:

`dnf info {{paquet}}`

- Instal·la un nou paquet:

`sudo dnf install {{paquet1 paquet2 ...}}`

- Desinstal·la un paquet:

`sudo dnf remove {{paquet1 paquet2 ...}}`

- Llista tots els paquets instal·lats:

`dnf list --installed`

- Troba quin paquet proveeeix un arxiu determinat:

`dnf provides {{arxiu}}`
