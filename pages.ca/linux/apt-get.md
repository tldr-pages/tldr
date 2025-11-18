# apt-get

> Eina de gestió de paquets per a distribucions basades en Debian.
> Busca paquets utilizant `apt-cache`.
> Més informació: <https://manned.org/apt-get.8>.

- Actualitza la llista de paquets i versions disponibles (es recomana executar aquest comandament abans que qualsevol altre `apt-get`):

`sudo apt-get update`

- Instala un paquet o l'actualitza a l'última versió disponible:

`sudo apt-get install {{paquet}}`

- Elimina un paquet:

`sudo apt-get remove {{paquet}}`

- Elimina un paquet i els seus arxius de configuració:

`sudo apt-get purge {{paquet}}`

- Actualitza tots els paquets instal·lats a les noves versions disponibles:

`sudo apt-get upgrade`

- Neteja el repositori local - eliminant fitxers de paquet (`.deb`) de descàrregues interrompudes que ja no es poden descarregar:

`apt-get autoclean`

- Elimina tots els paquets inneccessaris:

`sudo apt-get autoremove`

- Actualitza paquets instal·lats (com `upgrade`), però elimina els paquets obsolets i instal·la paquets adicionals per satisfer les dependències:

`sudo apt-get dist-upgrade`
