# ldapsearch

> CLI utility for querying an LDAP directory.

- Query LDAP for all items that match filter "{{memberOf}}={{group1}}" and return {{displayName}}:

`ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} -b {{base_ou}} '{{memberOf}}={{group1}}' {{displayName}}`

- Query LDAP with a no-newline password file and return {{displayName}}:

`ldapsearch -D '{{admin_DN}}' -y '{{password_file}}' -h {{ldap_host}} -b {{base_ou}} '{{memberOf}}={{group1}}' {{displayName}}`

- Return the first 5 items that match the given filter:

`ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} -b {{base_ou}} '{{memberOf}}={{group1}}' -z 5 {{displayName}}`

- Query LDAP for up-to 7 seconds for all items that match filter "{{memberOf}}={{group1}}" and return {{displayName}}:

`ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} -b {{base_ou}} '{{memberOf}}={{group1}}' -l 7 {{displayName}}`

- Query LDAP for all items that DO NOT match filter "{{memberOf}}={{group1}}" and return {{displayName}}:

`ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} -b {{base_ou}} '(!({{memberOf}}={{group1}}))' {{displayName}}`

- Query LDAP for all items that match filter "memberOf=group1 AND memberOf=group2 AND memberOf=group3" and return {{displayName}} value for each item:

`ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} '(&(memberOf=group1)(memberOf=group2)(memberOf=group3))' "{{displayName}}"`

- Query LDAP for all items that match filter "memberOf=group1 OR memberOf=group2 OR memberOf=group3" and return {{displayName}} value for each item:

`ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} '(|(memberOf=group1)(memberOf=group1)(memberOf=group3))' {{displayName}}`

- Query LDAP for all items that match filter "memberOf=group1 AND memberOf=group2 AND NOT memberOf=group3" and return {{displayName}} value for each item:

`ldapsearch -D '{{admin_DN}}' -w '{{password}}' -h {{ldap_host}} '(&(memberOf=group1)(memberOf=group2)(!(memberOf=group3)))' {{displayName}}`
