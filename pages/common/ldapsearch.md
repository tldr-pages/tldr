# ldapsearch

> Query an LDAP directory.
> More information: <https://docs.ldap.com/ldap-sdk/docs/tool-usages/ldapsearch.html>.

- Query an LDAP server for all items that are a member of the given group and return the object's displayName value:

`ldapsearch {{[-D|--bindDN]}} '{{admin_DN}}' {{[-w|--bindPassword]}} '{{password}}' {{[-h|--hostname]}} {{ldap_host}} {{[-b|--baseDN]}} {{base_ou}} '{{memberOf=group1}}' displayName`

- Query an LDAP server with a no-newline password file for all items that are a member of the given group and return the object's displayName value:

`ldapsearch  {{[-D|--bindDN]}} '{{admin_DN}}' {{[-u|--keyStorePasswordFile]}} '{{password_file}}' {{[-h|--hostname]}} {{ldap_host}} {{[-b|--baseDN]}} {{base_ou}} '{{memberOf=group1}}' displayName`

- Return 5 items that match the given filter:

`ldapsearch  {{[-D|--bindDN]}} '{{admin_DN}}' {{[-w|--bindPassword]}} '{{password}}' {{[-h|--hostname]}} {{ldap_host}} {{[-b|--baseDN]}} {{base_ou}} '{{memberOf=group1}}' {{[-z|--sizeLimit]}} 5 displayName`

- Wait up to 7 seconds for a response:

`ldapsearch  {{[-D|--bindDN]}} '{{admin_DN}}' {{[-w|--bindPassword]}} '{{password}}' {{[-h|--hostname]}} {{ldap_host}} {{[-b|--baseDN]}} {{base_ou}} '{{memberOf=group1}}' {{[-l|--timeLimitSeconds]}} 7 displayName`

- Invert the filter:

`ldapsearch  {{[-D|--bindDN]}} '{{admin_DN}}' {{[-w|--bindPassword]}} '{{password}}' {{[-h|--hostname]}} {{ldap_host}} {{[-b|--baseDN]}} {{base_ou}} '(!(memberOf={{group1}}))' displayName`

- Return all items that are part of multiple groups, returning the display name for each item:

`ldapsearch  {{[-D|--bindDN]}} '{{admin_DN}}' {{[-w|--bindPassword]}} '{{password}}' {{[-h|--hostname]}} {{ldap_host}} '(&({{memberOf=group1}})({{memberOf=group2}})({{memberOf=group3}}))' "displayName"`

- Return all items that are members of at least 1 of the specified groups:

`ldapsearch  {{[-D|--bindDN]}} '{{admin_DN}}' {{[-w|--bindPassword]}} '{{password}}' {{[-h|--hostname]}} {{ldap_host}} '(|({{memberOf=group1}})({{memberOf=group1}})({{memberOf=group3}}))' displayName`

- Combine multiple boolean logic filters:

`ldapsearch  {{[-D|--bindDN]}} '{{admin_DN}}' {{[-w|--bindPassword]}} '{{password}}' {{[-h|--hostname]}} {{ldap_host}} '(&({{memberOf=group1}})({{memberOf=group2}})(!({{memberOf=group3}})))' displayName`
