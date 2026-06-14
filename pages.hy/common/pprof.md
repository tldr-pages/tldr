# պրոֆ

> Պատկերացրեք և վերլուծեք պրոֆիլավորման տվյալները:.
> Լրացուցիչ տեղեկություններ. <https://github.com/google/pprof/tree/main/doc#pprof>:.

- Ստեղծեք տեքստային զեկույց հատուկ պրոֆիլավորման ֆայլից, fibbo երկուական տարբերակով.:

`pprof -top {{./fibbo}} {{./fibbo-profile.pb.gz}}`

- Ստեղծեք գրաֆիկ և բացեք այն վեբ բրաուզերում.:

`pprof -svg {{./fibbo}} {{./fibbo-profile.pb.gz}}`

- Գործարկեք pprof-ը ինտերակտիվ ռեժիմով, որպեսզի կարողանաք ձեռքով գործարկել `pprof` ֆայլը.:

`pprof {{./fibbo}} {{./fibbo-profile.pb.gz}}`

- Գործարկեք վեբ սերվեր, որը սպասարկում է վեբ ինտերֆեյս `pprof`-ի վերևում:

`pprof -http={{localhost:8080}} {{./fibbo}} {{./fibbo-profile.pb.gz}}`

- Վերցրեք պրոֆիլը HTTP սերվերից և ստեղծեք հաշվետվություն.:

`pprof {{http://localhost:8080/debug/pprof}}`
