# elasticsearch-saml-metadata

> Ստեղծեք SAML Ծառայությունների Մատակարարի մետատվյալներ SAML ինքնության մատակարարի կազմաձևման համար:.
> Լրացուցիչ տեղեկություններ. <https://www.elastic.co/docs/reference/elasticsearch/command-line-tools/saml-metadata>:.

- Ստեղծեք SAML մետատվյալներ որոշակի ոլորտի համար և տպեք դրանք `stdout`-ում:

`elasticsearch-saml-metadata --realm {{realm_name}}`

- Ստեղծեք SAML մետատվյալներ և գրեք դրանք որոշակի ֆայլում.:

`elasticsearch-saml-metadata --realm {{realm_name}} --out {{path/to/file.xml}}`

- Ցուցադրել օգնությունը.:

`elasticsearch-saml-metadata {{[-h|--help]}}`
