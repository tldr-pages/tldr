# ldapdomaindump

> Felhasználók, számítógépek, csoportok, operációs rendszerek és tagsági információk LDAP-on keresztül HTML, JSON és greppelhető kimenetekbe történő kiírása. Lásd még: `ldapsearch`. További információ: <https://github.com/dirkjanm/ldapdomaindump>.

- A megadott LDAP-fiókot használó összes információ kiírása:

`ldapdomaindump --user {{domain}}\\{{administrator}} --password {{password|ntlm_hash}} {{hostname|ip}}`

- Minden információ kiírása, a számítógépek hostneveinek feloldásával:

`ldapdomaindump --resolve --user {{domain}}\\{{administrator}} --password {{password}} {{hostname|ip}}`

- Minden információ kiírása, a számítógép hostneveinek feloldása a kiválasztott DNS-kiszolgálóval:

`ldapdomaindump --resolve --dns-server {{domain_controller_ip}} --user {{domain}}\\{{administrator}} --password {{password}} {{hostname|ip}}`

- Minden információ kiürítése a megadott könyvtárba JSON-kimenet nélkül:

`ldapdomaindump --no-json --outdir {{path/to/directory}} --user {{domain}}\\{{administrator}} --password {{password}} {{hostname|ip}}`
