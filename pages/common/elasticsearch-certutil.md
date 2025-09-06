# elasticsearch-certutil

> Generate and manage SSL certificates for Elasticsearch security.
> More information: <https://www.elastic.co/guide/en/elasticsearch/reference/current/certutil.html>.

- Generate a new Certificate Authority (CA) with default options:

`elasticsearch-certutil ca`

- Generate a new certificate using the built-in CA:

`elasticsearch-certutil cert`

- Generate certificates non-interactively and output PEM files:

`elasticsearch-certutil cert {{[-s|--silent]}} --pem`

- Generate HTTP certificates with the built-in CA:

`elasticsearch-certutil http`

- Generate transport certificates non-interactively:

`elasticsearch-certutil transport {{[-s|--silent]}}`

- Generate a certificate signing request (CSR):

`elasticsearch-certutil csr`

- Generate encrypted keystore passwords:

`elasticsearch-certutil password`

- Generate a keystore password with a specified value:

`elasticsearch-certutil password --pass {{password}}`
