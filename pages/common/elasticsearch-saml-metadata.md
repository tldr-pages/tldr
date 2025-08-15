# elasticsearch-saml-metadata

> Generate SAML Service Provider metadata for configuring a SAML Identity Provider.
> More information: <https://www.elastic.co/guide/en/elasticsearch/reference/current/saml-metadata.html>.

- Generate SAML metadata for a specific realm and print it to `stdout`:

`elasticsearch-saml-metadata --realm {{realm_name}}`

- Generate SAML metadata and write it to a specific file:

`elasticsearch-saml-metadata --realm {{realm_name}} --out {{path/to/file.xml}}`

- Display help:

`elasticsearch-saml-metadata {{[-h|--help]}}`
