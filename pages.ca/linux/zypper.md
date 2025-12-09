# zypper

> Utilitat per la gestió de paquets en SUSE i openSUSE.
> Més informació: <https://en.opensuse.org/SDB:Zypper_manual>.

- Sincronitza la llista de paquets i versions disponibles:

`zypper refresh`

- Instal·la un nou paquet:

`zypper install {{paquet}}`

- Elimina un paquet:

`zypper remove {{paquet}}`

- Actualitza els paquets instal·lats a la versió més recent disponible:

`zypper update`

- Busca en els repositoris un paquet mitjançant una paraula clau:

`zypper search {{paraula_clau}}`

- Mostra informació relacionada amb els repositoris configurats:

`zypper repos --sort-by-priority`
