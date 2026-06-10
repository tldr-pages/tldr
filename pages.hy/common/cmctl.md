# cmctl

> Կառավարեք վկայական-մենեջերի ռեսուրսները ձեր կլաստերի ներսում:.
> Ստուգեք վկայագրի ստորագրման կարգավիճակը, հաստատեք/մերժեք հարցումները և թողարկեք նոր վկայականի հարցումներ:.
> Լրացուցիչ տեղեկություններ. <https://cert-manager.io/docs/reference/cmctl/>:.

- Ստուգեք, արդյոք cert-manager API-ն պատրաստ է.:

`cmctl check api`

- Ստուգեք վկայագրի կարգավիճակը.:

`cmctl status certificate {{cert_name}}`

- Ստեղծեք նոր վկայականի հարցում՝ հիմնվելով գոյություն ունեցող վկայագրի վրա.:

`cmctl create certificaterequest my-cr --from-certificate-file {{cert.yaml}}`

- Ստեղծեք նոր վկայականի հարցում, վերցրեք ստորագրված վկայականը և սահմանեք սպասման առավելագույն ժամանակը.:

`cmctl create certificaterequest my-cr --from-certificate-file {{cert.yaml}} --fetch-certificate --timeout {{20m}}`
