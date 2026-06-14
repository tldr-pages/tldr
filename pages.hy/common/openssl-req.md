# openssl պահանջ

> Կառավարեք PKCS#10 վկայագրի ստորագրման հարցումները:.
> Լրացուցիչ տեղեկություններ. <https://docs.openssl.org/master/man1/openssl-req/>:.

- Ստեղծեք վկայագրի ստորագրման հարցում, որը կուղարկվի սերտիֆիկատի մարմնին.:

`openssl req -new -sha256 -key {{filename.key}} -out {{filename.csr}}`

- Ստեղծեք ինքնաստորագրված վկայագիր և համապատասխան բանալիների զույգ՝ երկուսն էլ ֆայլում պահելով.:

`openssl req -new -x509 -newkey {{rsa}}:{{4096}} -keyout {{filename.key}} -out {{filename.cert}} -subj "{{/C=XX/CN=foobar}}" -days {{365}}`
