# քառ

> Ժամանակակից OpenPGP հրամանի տող գործիք:.
> Տես նաև՝ `gpg`:.
> Լրացուցիչ տեղեկություններ. <https://sequoia-pgp.gitlab.io/sequoia-sq/man/sq.1.html>:.

- Գաղտնագրեք ֆայլը՝ օգտագործելով գաղտնաբառ (սիմետրիկ գաղտնագրում).:

`sq encrypt --with-password --without-signature {{path/to/file}} --output {{path/to/file.pgp}}`

- Ապակոդավորել գաղտնաբառով պաշտպանված ֆայլը.:

`sq decrypt {{path/to/file.pgp}} --output {{path/to/file}}`

- Ստուգեք OpenPGP ֆայլը՝ դրա մետատվյալներն ու կառուցվածքը տեսնելու համար.:

`sq inspect {{path/to/file.pgp}}`

- Ստուգեք ֆայլը անջատված ստորագրությամբ և վկայականի ֆայլով.:

`sq verify --signer-file {{path/to/signer.asc}} --signature-file {{path/to/file.sig}} {{path/to/file}}`

- Ստուգեք ֆայլը ներկառուցված (հստակ տեքստ) ստորագրությամբ և վկայականի ֆայլով.:

`sq verify --signer-file {{path/to/signer.asc}} --cleartext {{path/to/file}}`

- Ստեղծեք ձեր սեփական բանալին և պահեք այն տեղական բանալիների խանութում.:

`sq key generate --own-key --name {{name}} --email {{name@example.com}}`

- Թվարկեք բոլոր գաղտնի բանալիները կամ վկայագրերը, որոնք կառավարվում են տեղական բանալիների խանութի կողմից.:

`sq {{key|cert}} list`

- Թվարկեք ընթացիկ կազմաձևման և պահպանման ուղիները.:

`sq config inspect paths`
