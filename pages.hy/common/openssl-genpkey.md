# openssl genpkey

> Ստեղծեք ասիմետրիկ բանալիների զույգեր:.
> Լրացուցիչ տեղեկություններ. <https://docs.openssl.org/master/man1/openssl-genpkey/>:.

- Ստեղծեք 2048 բիթանոց RSA մասնավոր բանալի՝ այն պահելով որոշակի ֆայլում.:

`openssl genpkey -algorithm rsa -pkeyopt rsa_keygen_bits:{{2048}} -out {{path/to/private.key}}`

- Ստեղծեք էլիպսային կորի մասնավոր բանալի՝ օգտագործելով `prime256v1` կորը՝ այն պահելով որոշակի ֆայլում՝:

`openssl genpkey -algorithm EC -pkeyopt ec_paramgen_curve:{{prime256v1}} -out {{path/to/private.key}}`

- Ստեղծեք `ED25519` էլիպսաձեւ կորի անձնական բանալի՝ այն պահելով որոշակի ֆայլում՝:

`openssl genpkey -algorithm {{ED25519}} -out {{path/to/private.key}}`
