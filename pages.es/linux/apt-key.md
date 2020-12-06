# apt-key

> Herramienta para la gestión de claves para el Gestor de Paquetes APT (APT Package Manager) en Debian y Ubuntu.

- Muestra las claves de confianza:

`apt-key list`

- Añade una clave al almacén de claves de confianza):

`apt-key add {{archivo_clave_pública.asc}}`

- Borrar una clave del almacén de claves de confianza:

`apt-key del {{id_clave}}`

- Añadir un clave remota al almacén de claves de confianza:

`wget -qO - {{https://host.tld/archivo.clave}} | apt-key add -`

- Añadir una clave de un servidor de claves con el identificador de la clave:

`apt-key adv --keyserver {{pgp.mit.edu}} --recv {{id_clave}}`
