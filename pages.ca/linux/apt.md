# apt

> Eina de gestió de paquets per a distribucions basades en Debian.
> Es recomana substituïr-lo per `apt-get` quan es faci servir interactivament en Ubuntu 16.04 o en versions posteriors.
> Més informació: <https://manpages.debian.org/latest/apt/apt.8.html>.

- Actualitza la llista de paquets i versions disponbles (es recomana executar aquest comandament abans que qualsevol altre `apt`):

`sudo apt update`

- Busca un paquet:

`apt search {{paquet}}`

- Mostra la informació de un paquet:

`apt show {{paquet}}`

- Instala un paquet o l'actualitza a l'última versió disponible:

`sudo apt install {{paquet}}`

- Elimina un paquet (si s'utiliza `purge` també elimina els seus arxius de configuració):

`sudo apt remove {{paquet}}`

- Actualitza tots els paquets instal·lats a les noves versions disponibles:

`sudo apt upgrade`

- Mostra tots els paquets:

`apt list`

- Mostra tots els paquets instalats:

`apt list --installed`
