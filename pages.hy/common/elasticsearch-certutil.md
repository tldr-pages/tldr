# elasticsearch-certutil

> Ստեղծեք և կառավարեք SSL վկայագրեր Elasticsearch-ի անվտանգության համար:.
> Լրացուցիչ տեղեկություններ. <https://www.elastic.co/docs/reference/elasticsearch/command-line-tools/certutil>:.

- Ստեղծեք նոր վկայականի մարմին (CA) լռելյայն ընտրանքներով.:

`elasticsearch-certutil ca`

- Ստեղծեք նոր վկայագիր՝ օգտագործելով ներկառուցված CA.:

`elasticsearch-certutil cert`

- Ստեղծեք վկայագրեր ոչ ինտերակտիվ կերպով և թողարկեք PEM ֆայլեր.:

`elasticsearch-certutil cert {{[-s|--silent]}} --pem`

- Ստեղծեք HTTP վկայագրեր ներկառուցված CA-ով.:

`elasticsearch-certutil http`

- Ստեղծեք տրանսպորտային վկայագրեր ոչ ինտերակտիվ կերպով.:

`elasticsearch-certutil transport {{[-s|--silent]}}`

- Ստեղծեք վկայագրի ստորագրման հարցում (CSR).:

`elasticsearch-certutil csr`

- Ստեղծեք կոդավորված բանալիների գաղտնաբառեր.:

`elasticsearch-certutil password`

- Ստեղծեք keystore-ի գաղտնաբառ՝ նշված արժեքով.:

`elasticsearch-certutil password --pass {{password}}`
