# authconfig

> CLI-felület a rendszer hitelesítési erőforrásainak konfigurálásához. További információ: <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system-level_authentication_guide/authconfig-install>.

- Az aktuális konfiguráció megjelenítése (vagy szárazfutás):

`authconfig --test`

- A kiszolgáló konfigurálása egy másik jelszófeltörő algoritmus használatára:

`authconfig --update --passalgo={{algorithm}}`

- Az LDAP-hitelesítés engedélyezése:

`authconfig --update --enableldapauth`

- Az LDAP-hitelesítés letiltása:

`authconfig --update --disableldapauth`

- Hálózati információs szolgáltatás (NIS) engedélyezése:

`authconfig --update --enablenis`

- Kerberos engedélyezése:

`authconfig --update --enablekrb5`

- Winbind (Active Directory) hitelesítés engedélyezése:

`authconfig --update --enablewinbindauth`

- Helyi engedélyezés engedélyezése:

`authconfig --update --enablelocauthorize`
