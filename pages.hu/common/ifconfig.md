# ifconfig

> Network Interface Configurator. További információ: <https://net-tools.sourceforge.io/man/ifconfig.8.html>.

- Ethernet-adapter hálózati beállításainak megtekintése:

`ifconfig eth0`

- Az összes interfész részleteinek megjelenítése, beleértve a letiltott interfészeket is:

`ifconfig -a`

- Az eth0 interfész letiltása:

`ifconfig eth0 down`

- Eth0 interfész engedélyezése:

`ifconfig eth0 up`

- IP-cím hozzárendelése az eth0 interfészhez:

`ifconfig eth0 {{ip_address}}`
