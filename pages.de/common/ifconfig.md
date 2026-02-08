# ifconfig

> Netzwerk-Interface-Konfigurator.
> Weitere Informationen: <https://net-tools.sourceforge.io/man/ifconfig.8.html>.

- Zeige die Netzwerkeinstellungen eines Interfaces:

`ifconfig {{interface_name}}`

- Zeige Details aller Interfaces, einschließlich deaktivierter Interfaces:

`ifconfig -a`

- Deaktiviere ein Interface:

`ifconfig {{interface_name}} down`

- Aktiviere ein Interface:

`ifconfig {{interface_name}} up`

- Weise einem Interface eine IP-Adresse zu:

`ifconfig {{interface_name}} {{ip_adresse}}`
