# openssl

> OpenSSL ծածկագրային գործիքակազմ:.
> Որոշ ենթահրամաններ, ինչպիսիք են `req`-ն, ունեն իրենց օգտագործման փաստաթղթերը:.
> Լրացուցիչ տեղեկություններ. <https://docs.openssl.org/master/man1/openssl/>:.

- Ստեղծեք անձնական բանալի և գաղտնագրեք ելքային ֆայլը՝ օգտագործելով AES-256:

`openssl genpkey -algorithm {{rsa|ec}} -out {{path/to/private.key}} -aes256`

- Ստեղծեք համապատասխան հանրային բանալին `private.key` մասնավոր բանալիից՝ օգտագործելով `rsa`:

`openssl rsa -in {{path/to/private.key}} -pubout -out {{path/to/public.key}}`

- Ստեղծեք ինքնստորագրված վկայագիր, որը վավեր է որոշակի օրերի համար (365).:

`openssl req -new -x509 -key {{path/to/private.key}} -out {{path/to/certificate.crt}} -days 365`

- Վերափոխեք վկայագիրը `.pem` կամ `.der` ձևաչափի.:

`openssl x509 -in {{path/to/certificate.crt}} -out {{path/to/certificate.pem|path/to/certificate.der}} -outform {{pem|der}}`

- Ստուգեք վկայագրի մանրամասները.:

`openssl x509 -in {{path/to/certificate.crt}} -text -noout`

- Ստեղծեք վկայագրի ստորագրման հարցում (CSR).:

`openssl req -new -key {{path/to/private.key}} -out {{path/to/request.csr}}`

- Ցուցադրել օգնությունը.:

`openssl help`

- Ցուցադրման տարբերակը:

`openssl version`
