# apt-mark

> Eina per canviar l'estat dels paquets instal·lats.
> Més informació: <https://manpages.debian.org/latest/apt/apt-mark.8.html>.

- Marca un paquet com a instal·lat automàticament:

`sudo apt-mark auto {{nom_paquet}}`

- Manté un paquet en la seva versió actual i evita que s'actualitzi:

`sudo apt-mark hold {{nom_paquet}}`

- Permet que es pugui actualitzar de nou:

`sudo apt-mark unhold {{nom_paquet}}`

- Mostra els paquets instal·lats manualment:

`apt-mark showmanual`

- Mostra els paquets mantinguts que no estàn actualitzats:

`apt-mark showhold`
