# openssl genrsa

> Ստեղծեք RSA մասնավոր բանալիներ:.
> Լրացուցիչ տեղեկություններ. <https://docs.openssl.org/master/man1/openssl-genrsa/>:.

- Ստեղծեք RSA մասնավոր բանալի 2048 բիթից մինչև `stdout`:

`openssl genrsa`

- Պահպանեք կամայական թվով բիթերի RSA մասնավոր բանալի ելքային ֆայլում.:

`openssl genrsa -out {{output_file.key}} {{1234}}`

- Ստեղծեք RSA մասնավոր բանալի և գաղտնագրեք այն AES256-ով (ձեզանից կպահանջվի մուտքի արտահայտություն).:

`openssl genrsa {{-aes256}}`
