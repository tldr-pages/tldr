# openssl x509

> Կառավարեք X.509 վկայականները:.
> Լրացուցիչ տեղեկություններ. <https://docs.openssl.org/master/man1/openssl-x509/>:.

- Ցուցադրել վկայականի տվյալները.:

`openssl x509 -in {{filename.crt}} -noout -text`

- Ցուցադրել վկայագրի գործողության ժամկետը.:

`openssl x509 -enddate -noout -in {{filename.pem}}`

- Փոխակերպեք վկայագիրը երկուական DER կոդավորման և տեքստային PEM կոդավորման միջև.:

`openssl x509 -inform {{der}} -outform {{pem}} -in {{original_certificate_file}} -out {{converted_certificate_file}}`

- Պահպանեք վկայագրի հանրային բանալին ֆայլում՝:

`openssl x509 -in {{certificate_file}} -noout -pubkey -out {{output_file}}`
