# openssl dgst

> Ստեղծեք մարսողական արժեքներ և կատարեք ստորագրության գործողություններ:.
> Լրացուցիչ տեղեկություններ. <https://docs.openssl.org/master/man1/openssl-dgst/>:.

- Հաշվեք SHA256-ի ամփոփումը ֆայլի համար՝ արդյունքը պահելով որոշակի ֆայլում.:

`openssl dgst -sha256 -binary -out {{output_file}} {{input_file}}`

- Ստորագրեք ֆայլ RSA ստեղնով, արդյունքը պահելով որոշակի ֆայլում.:

`openssl dgst -sign {{private_key_file}} -sha256 -sigopt rsa_padding_mode:pss -out {{output_file}} {{input_file}}`

- Ստուգեք RSA ստորագրությունը.:

`openssl dgst -verify {{public_key_file}} -signature {{signature_file}} -sigopt rsa_padding_mode:pss {{signature_message_file}}`

- Ստորագրեք ֆայլը օգտագործելով և ECDSA բանալի.:

`openssl dgst -sign {{private_key_file}} -sha256 -out {{output_file}} {{input_file}}`

- Ստուգեք ECDSA ստորագրությունը.:

`openssl dgst -verify {{public_key_file}} -signature {{signature_file}} {{signature_message_file}}`
