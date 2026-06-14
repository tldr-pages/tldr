# բացսսլ ց

> Ստեղծեք և ստուգեք ժամանակի դրոշմակնիքները:.
> Լրացուցիչ տեղեկություններ. <https://docs.openssl.org/master/man1/openssl-ts/>:.

- Ստեղծեք SHA-512 ժամանակի դրոշմակնիքի հարցում կոնկրետ ֆայլի համար և թողարկեք `file.tsq`:

`openssl ts -query -data {{path/to/file}} -sha512 -out {{path/to/file.tsq}}`

- Ստուգեք կոնկրետ ժամանակացույցի պատասխան ֆայլի ամսաթիվը և մետատվյալները.:

`openssl ts -reply -in {{path/to/file.tsr}} -text`

- Ստուգեք ժամանակի դրոշմանիշի հարցման ֆայլը և ժամանակի կնիքի պատասխանի ֆայլը սերվերից SSL վկայագրի ֆայլով.:

`openssl ts -verify -in {{path/to/file.tsr}} -queryfile {{path/to/file.tsq}} -partial_chain -CAfile {{path/to/cert.pem}}`

- Ստեղծեք հարցման ժամանակային կնիքի պատասխան՝ օգտագործելով բանալի և ստորագրման վկայական և թողարկեք այն `file.tsr`:

`openssl ts -reply -queryfile {{path/to/file.tsq}} -inkey {{path/to/tsakey.pem}} -signer tsacert.pem -out {{path/to/file.tsr}}`
