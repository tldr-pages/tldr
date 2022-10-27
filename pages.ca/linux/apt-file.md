# apt-file

> Busca arxius en paquets apt, incloent els que encara no s'han instal·lat.
> Més informació: <https://manpages.debian.org/latest/apt-file/apt-file.1.html>.

- Actualita les metadades de la base de dades:

`sudo apt update`

- Busca paquets que continguin l'arxiu o ruta especificada:

`apt-file search {{ruta/al/arxiu}}`

- Mostra el contingut del paquet especificat:

`apt-file list {{nom_paquet}}`

- Busca paquets que igualin l'expressió regular donada en `patró`:

`apt-file {{search|find}} --regexp {{expressió_regular}}`
