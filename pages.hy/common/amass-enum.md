# հավաքել թվով

> Գտեք տիրույթի ենթադոմեյնները:.
> Լրացուցիչ տեղեկություններ. <https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md#the-enum-subcommand>:.

- Գտեք (պասիվ) ենթադոմեյնները [d]տիրույթում.:

`amass enum -d {{domain_name}}`

- Գտեք [d] տիրույթի ենթադոմեյնները և ակտիվորեն ստուգեք դրանք՝ փորձելով լուծել գտնված ենթադոմեյնները.:

`amass enum -active -d {{domain_name}} -p {{80,443,8080}}`

- Կատարեք կոպիտ ուժի որոնում ենթա[d]տիրույթների համար.:

`amass enum -brute -d {{domain_name}}`

- Արդյունքները պահեք տեքստային ֆայլում.:

`amass enum -o {{output_file}} -d {{domain_name}}`

- Պահպանեք տերմինալի ելքը ֆայլում և այլ մանրամասն արդյունքներ գրացուցակում.:

`amass enum -o {{output_file}} -dir {{path/to/directory}} -d {{domain_name}}`

- Թվարկեք բոլոր առկա տվյալների աղբյուրները.:

`amass enum -list`
