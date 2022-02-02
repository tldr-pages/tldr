# apt-key

> Eina de gestió de claus per al Gestor de Paquets APT (APT Package Manager) en Debian i Ubuntu.
> Nota: `apt-key` és obsolet (excepte l'ús de `apt-key del` en scrits de mantenidor).
> Més informació: <https://manpages.debian.org/latest/apt/apt-key.8.html>.

- Mostra les claus de confiança:

`apt-key list`

- Afegeix una clau al magatzem de claus de confiança:

`apt-key add {{arxiu_clau_pública.asc}}`

- Borra una clau del magatzem de claus de confiança:

`apt-key del {{id_clau}}`

- Afegir una clau remota al magatzem de claus de confiança:

`wget -qO - {{https://host.tld/archiu.clau}} | apt-key add -`

- Afegir una clau d'un servidor de claus amb l'identificador de la clau:

`apt-key adv --keyserver {{pgp.mit.edu}} --recv {{id_clau}}`
