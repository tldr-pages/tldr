# ldapsearch

> Հարցրեք LDAP գրացուցակում:.
> Լրացուցիչ տեղեկություններ. <https://docs.ldap.com/ldap-sdk/docs/tool-usages/ldapsearch.html>:.

- Հարցրեք LDAP սերվեր բոլոր տարրերի համար, որոնք տվյալ խմբի անդամ են և վերադարձրեք օբյեկտի displayName արժեքը.:

`ldapsearch {{[-D|--bindDN]}} '{{admin_DN}}' {{[-w|--bindPassword]}} '{{password}}' {{[-h|--hostname]}} {{ldap_host}} {{[-b|--baseDN]}} {{base_ou}} '{{memberOf=group1}}' displayName`

- Հարցրեք LDAP սերվերին առանց նոր տող գաղտնաբառի ֆայլի բոլոր տարրերի համար, որոնք տվյալ խմբի անդամ են և վերադարձնում են օբյեկտի displayName արժեքը.:

`ldapsearch {{[-D|--bindDN]}} '{{admin_DN}}' {{[-u|--keyStorePasswordFile]}} '{{password_file}}' {{[-h|--hostname]}} {{ldap_host}} {{[-b|--baseDN]}} {{base_ou}} '{{memberOf=group1}}' displayName`

- Վերադարձեք 5 տարր, որոնք համապատասխանում են տվյալ ֆիլտրին.:

`ldapsearch {{[-D|--bindDN]}} '{{admin_DN}}' {{[-w|--bindPassword]}} '{{password}}' {{[-h|--hostname]}} {{ldap_host}} {{[-b|--baseDN]}} {{base_ou}} '{{memberOf=group1}}' {{[-z|--sizeLimit]}} 5 displayName`

- Պատասխանի համար սպասեք մինչև 7 վայրկյան.:

`ldapsearch {{[-D|--bindDN]}} '{{admin_DN}}' {{[-w|--bindPassword]}} '{{password}}' {{[-h|--hostname]}} {{ldap_host}} {{[-b|--baseDN]}} {{base_ou}} '{{memberOf=group1}}' {{[-l|--timeLimitSeconds]}} 7 displayName`

- Շրջեք զտիչը.:

`ldapsearch {{[-D|--bindDN]}} '{{admin_DN}}' {{[-w|--bindPassword]}} '{{password}}' {{[-h|--hostname]}} {{ldap_host}} {{[-b|--baseDN]}} {{base_ou}} '(!(memberOf={{group1}}))' displayName`

- Վերադարձրեք բոլոր տարրերը, որոնք մի քանի խմբերի մաս են կազմում՝ վերադարձնելով յուրաքանչյուր տարրի ցուցադրվող անունը.:

`ldapsearch {{[-D|--bindDN]}} '{{admin_DN}}' {{[-w|--bindPassword]}} '{{password}}' {{[-h|--hostname]}} {{ldap_host}} '(&({{memberOf=group1}})({{memberOf=group2}})({{memberOf=group3}}))' "displayName"`

- Վերադարձրեք բոլոր ապրանքները, որոնք նշված խմբերից առնվազն 1-ի անդամ են.:

`ldapsearch {{[-D|--bindDN]}} '{{admin_DN}}' {{[-w|--bindPassword]}} '{{password}}' {{[-h|--hostname]}} {{ldap_host}} '(|({{memberOf=group1}})({{memberOf=group1}})({{memberOf=group3}}))' displayName`

- Միավորել բազմաթիվ բուլյան տրամաբանական զտիչներ.:

`ldapsearch {{[-D|--bindDN]}} '{{admin_DN}}' {{[-w|--bindPassword]}} '{{password}}' {{[-h|--hostname]}} {{ldap_host}} '(&({{memberOf=group1}})({{memberOf=group2}})(!({{memberOf=group3}})))' displayName`
