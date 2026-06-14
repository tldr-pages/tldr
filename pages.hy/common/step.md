# քայլ

> Հեշտ օգտագործվող CLI գործիք Հանրային բանալիների ենթակառուցվածքի (PKI) համակարգերի և աշխատանքային հոսքերի կառուցման, շահագործման և ավտոմատացման համար:.
> Տես նաև՝ `openssl`:.
> Լրացուցիչ տեղեկություններ. <https://smallstep.com/docs/step-cli/>:.

- Ստուգեք վկայագրի բովանդակությունը.:

`step certificate inspect {{path/to/certificate.crt}}`

- Ստեղծեք արմատային CA վկայագիր և բանալի (ավելացրեք `--no-password --insecure`՝ անձնական բանալու գաղտնաբառի պաշտպանությունը բաց թողնելու համար):

`step certificate create "{{Example Root CA}}" {{path/to/root-ca.crt}} {{path/to/root-ca.key}} --profile root-ca`

- Ստեղծեք վկայագիր կոնկրետ հոսթի անվան համար և ստորագրեք այն արմատային CA-ով (CSR-ի ստեղծումը կարելի է բաց թողնել պարզեցման համար).:

`step certificate create {{hostname.example.com}} {{path/to/hostname.crt}} {{path/to/hostname.key}} --profile leaf --ca {{path/to/root-ca.crt}} --ca-key {{path/to/root-ca.key}}`

- Ստուգեք վկայագրի շղթան.:

`step certificate verify {{path/to/hostname.crt}} --roots {{path/to/root-ca.crt}} --verbose`

- Փոխակերպեք PEM ձևաչափի վկայագիրը DER-ի և գրեք այն սկավառակի վրա.:

`step certificate format {{path/to/certificate.pem}} --out {{path/to/certificate.der}}`

- Տեղադրեք կամ տեղահանեք արմատային վկայագիրը համակարգի կանխադրված վստահության խանութում.:

`step certificate {{install|uninstall}} {{path/to/root-ca.crt}}`

- Ստեղծեք RSA/EC մասնավոր և հանրային ստեղնաշար (ավելացրեք `--no-password --insecure`՝ անձնական բանալու գաղտնաբառի պաշտպանությունը բաց թողնելու համար).:

`step crypto keypair {{path/to/public_key}} {{path/to/private_key}} --kty {{RSA|EC}}`

- Ցուցադրել օգնություն ենթահրամանների համար.:

`step {{path|base64|certificate|completion|context|crl|crypto|oauth|ca|beta|ssh}} --help`
