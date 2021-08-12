# ldapsearch

> Utilitar CLI pentru interogarea unui director LDAP.

- Interogare un server LDAP pentru toate elementele care sunt un membru al grupului dat și returnează valoarea DisplayName obiectului:

`ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} -b {{base_ou}} '{{memberOf=group1}}' displayName`

- Interogare un server LDAP cu un fișier parolă fără newline pentru toate elementele care sunt un membru al grupului dat și returnează valoarea DisplayName obiectului:

`ldapsearch -D '{{admin_DN}}' -y '{{password_file}}' -h {{ldap_host}} -b {{base_ou}} '{{memberOf=group1}}' displayName`

- Returnați 5 elemente care se potrivesc cu filtrul dat:

`ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} -b {{base_ou}} '{{memberOf=group1}}' -z 5 displayName`

- Așteptați până la 7 secunde pentru un răspuns:

`ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} -b {{base_ou}} '{{memberOf=group1}}' -l 7 displayName`

- Inversează filtrul:

`ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} -b {{base_ou}} '(!(memberOf={{group1}}))' displayName`

- Returnați toate elementele care fac parte din mai multe grupuri, returnând numele afișat pentru fiecare element:

`ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} '(&({{memberOf=group1}})({{memberOf=group2}})({{memberOf=group3}}))' "displayName"`

- Returnați toate elementele care sunt membri ai cel puțin 1 din grupurile specificate:

`ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} '(|({{memberOf=group1}})({{memberOf=group1}})({{memberOf=group3}}))' displayName`

- Combinați mai multe filtre logice booleene:

`ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} '(&({{memberOf=group1}})({{memberOf=group2}})(!({{memberOf=group3}})))' displayName`
