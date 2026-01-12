# zypper

> Utilitat per la gestió de paquets en SUSE i openSUSE.
> Més informació: <https://en.opensuse.org/SDB:Zypper_manual>.

- Sincronitza la llista de paquets i versions disponibles:

`sudo zypper {{[ref|refresh]}}`

- Instal·la un nou paquet:

`sudo zypper {{[in|install]}} {{paquet}}`

- Elimina un paquet:

`sudo zypper {{[rm|remove]}} {{paquet}}`

- Actualitza els paquets instal·lats a la versió més recent disponible:

`sudo zypper {{[up|update]}}`

- Busca en els repositoris un paquet mitjançant una paraula clau:

`zypper {{[se|search]}} {{paraula_clau}}`

- Mostra informació relacionada amb els repositoris configurats:

`zypper {{[lr|repos]}} --sort-by-priority`
