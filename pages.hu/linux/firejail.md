# firejail

> Biztonságosan homokdobozolja a folyamatokat a konténerekbe a beépített Linux képességek segítségével. További információ: <https://manned.org/firejail>.

- Integrálja a firejailt az asztali környezetébe:

`sudo firecfg`

- Nyisson meg egy korlátozott Mozilla Firefoxot:

`firejail {{firefox}}`

- Indítson el egy korlátozott Apache-kiszolgálót egy ismert felületen és címen:

`firejail --net={{eth0}} --ip={{192.168.1.244}} {{/etc/init.d/apache2}} {{start}}`

- Futtatott homokozó dobozok listázása:

`firejail --list`

- A futó sandboxok hálózati tevékenységének listázása:

`firejail --netstats`

- Futó homokozó leállítása:

`firejail --shutdown={{7777}}`
