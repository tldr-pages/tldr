# apt-file

> Busca arxius en paquets APT, incloent els que encara no s'han instal·lat.
> Més informació: <https://manned.org/apt-file>.

- Actualita les metadades de la base de dades:

`sudo apt update`

- Busca paquets que continguin l'arxiu o ruta especificada:

`apt-file {{[find|search]}} {{ruta/al/arxiu}}`

- Mostra el contingut del paquet especificat:

`apt-file list {{nom_paquet}}`

- Busca paquets que igualin l'expressió regular donada en `patró`:

`apt-file {{[find|search]}} {{[-x|--regexp]}} {{expressió_regular}}`
