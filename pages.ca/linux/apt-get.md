# apt-get

> Eina de gestió de paquets per a distribucions basades en Debian.
> Busca paquets utilizant `apt-cache`.
> Més informació: <https://manpages.debian.org/latest/apt/apt-get.8.html>.

- Actualitza la llista de paquets i versions disponibles (es recomana executar aquest comandament abans que qualsevol altre `apt-get`):

`apt-get update`

- Instala un paquet o l'actualitza a l'última versió disponible:

`apt-get install {{paquet}}`

- Elimina un paquet:

`apt-get remove {{paquet}}`

- Elimina un paquet i els seus arxius de configuració:

`apt-get purge {{paquet}}`

- Actualitza tots els paquets instal·lats a les noves versions disponibles:

`apt-get upgrade`

- Neteja el repositori local - eliminant fitxers de paquet (`.deb`) de descàrregues interrompudes que ja no es poden descarregar:

`apt-get autoclean`

- Elimina tots els paquets inneccessaris:

`apt-get autoremove`

- Actualitza paquets instal·lats (com `upgrade`), però elimina els paquets obsolets i instal·la paquets adicionals per satisfer les dependències:

`apt-get dist-upgrade`
