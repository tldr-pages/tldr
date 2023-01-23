# ldapsearch

> CLI segédprogram LDAP könyvtár lekérdezésére. További információ: <https://docs.ldap.com/ldap-sdk/docs/tool-usages/ldapsearch.html>.

- Lekérdezi az LDAP-kiszolgálót az összes olyan elemről, amely a megadott csoport tagja, és visszaadja az objektum displayName értékét:

`ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} -b {{base_ou}} '{{memberOf=group1}}' displayName`

- Egy LDAP-kiszolgáló lekérdezése egy újsor nélküli jelszófájllal az adott csoporthoz tartozó összes elemre, és az objektum displayName értékének visszaadása:

`ldapsearch -D '{{admin_DN}}' -y '{{password_file}}' -h {{ldap_host}} -b {{base_ou}} '{{memberOf=group1}}' displayName`

- Az adott szűrőnek megfelelő 5 elem visszaadása:

`ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} -b {{base_ou}} '{{memberOf=group1}}' -z 5 displayName`

- Várjon legfeljebb 7 másodpercet a válaszra:

`ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} -b {{base_ou}} '{{memberOf=group1}}' -l 7 displayName`

- Fordítsa meg a szűrőt:

`ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} -b {{base_ou}} '(!(memberOf={{group1}}))' displayName`

- Visszaadja az összes olyan elemet, amely több csoport tagja, és minden egyes elemhez visszaadja a megjelenített nevet:

`ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} '(&({{memberOf=group1}})({{memberOf=group2}})({{memberOf=group3}}))' "displayName"`

- Az összes olyan elem visszaadása, amely legalább 1 megadott csoport tagja:

`ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} '(|({{memberOf=group1}})({{memberOf=group1}})({{memberOf=group3}}))' displayName`

- Több bólés logikai szűrő kombinálása:

`ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} '(&({{memberOf=group1}})({{memberOf=group2}})(!({{memberOf=group3}})))' displayName`
