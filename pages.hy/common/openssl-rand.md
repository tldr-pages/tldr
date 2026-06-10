# openssl ռանդ

> Ստեղծեք պատահական բայթեր՝ օգտագործելով գաղտնագրորեն ապահով PRNG:.
> Լրացուցիչ տեղեկություններ. <https://docs.openssl.org/master/man1/openssl-rand/>:.

- Ստեղծեք 8 բայթ (16 նիշ) վեցանկյուն տող և գրեք այն `stdout`-ում:

`openssl rand -hex 8`

- Ստեղծեք 20 պատահական բայթ, որոնք կոդավորված են base64-ում:

`openssl rand -base64 20`

- Ստեղծեք պատահական բայթեր և գրեք դրանք ֆայլում (առանց կոդավորման).:

`openssl rand -out {{path/to/file}} {{length}}`

- Ստեղծեք 1 KiB/MiB/GiB/TiB պատահական բայթ՝ կոդավորված hex/base64:

`openssl rand -{{hex|base64}} 1{{K|M|G|T}}`
