#զանգվածներ

> Լուծել DNS գրառումները մեծ քանակությամբ բարձր կատարողականությամբ հետախուզության համար:.
> Տես նաև՝ `dig`, `dnsx`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/blechschmidt/massdns#usage>:.

- Որոշել `A` գրառումները տիրույթների համար ֆայլում՝ օգտագործելով նշված լուծիչներ.:

`massdns {{[-r|--resolvers]}} {{path/to/resolvers.txt}} {{path/to/domains.txt}}`

- Լուծեք գրանցման որոշակի տեսակ և արդյունքները գրեք ֆայլում.:

`massdns {{[-r|--resolvers]}} {{path/to/resolvers.txt}} {{[-t|--type]}} {{A|AAAA|NS|MX|TXT}} {{[-w|--outfile]}} {{path/to/output.txt}} {{path/to/domains.txt}}`

- Լուծել տիրույթները պարզ տեքստի ելքային ձևաչափով.:

`massdns {{[-r|--resolvers]}} {{path/to/resolvers.txt}} {{[-o|--output]}} S {{path/to/domains.txt}}`

- Լուծել տիրույթները JSON ելքային ձևաչափով.:

`massdns {{[-r|--resolvers]}} {{path/to/resolvers.txt}} {{[-o|--output]}} J {{path/to/domains.txt}}`

- Լուծեք տիրույթները միաժամանակյա որոնումների հատուկ քանակով.:

`massdns {{[-r|--resolvers]}} {{path/to/resolvers.txt}} {{[-s|--hashmap-size]}} {{10000}} {{path/to/domains.txt}}`

- Լուծեք տիրույթները հանգիստ ռեժիմով, ճնշելով կարգավիճակի ելքը.:

`massdns {{[-r|--resolvers]}} {{path/to/resolvers.txt}} {{[-q|--quiet]}} {{path/to/domains.txt}}`
