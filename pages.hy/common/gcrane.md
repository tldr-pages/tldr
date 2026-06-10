#գրանց

> Կոնտեյների պատկերների կառավարման գործիք:.
> Այս գործիքն իրականացնում է `crane` հրամանների գերհամակարգը, լրացուցիչ հրամաններով, որոնք հատուկ են Google Container Registry-ին (`gcr.io`):.
> Որոշ ենթահրամաններ, ինչպիսիք են `append`, `auth`, `copy` և այլն, ունեն իրենց օգտագործման փաստաթղթերը, որոնք կարելի է գտնել `crane`-ում:.
> Որոշ ենթահրամաններ, ինչպիսիք են `completion`, `gc`, `help` հատուկ են gcrane-ին և ունեն իրենց օգտագործման փաստաթղթերը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>:.

- Մուտք գործեք ռեեստր.:

`gcrane auth login {{registry}} {{[-u|--username]}} {{user}} {{[-p|--password]}} {{password}}`

- Ցուցակել պիտակները, մանիֆեստները և ենթապահոցները.:

`gcrane ls {{registry}}/{{project_id}}`

- Պատճենել պատկերները մի ռեեստրից մյուսը.:

`gcrane cp {{[-r|--recursive]}} {{source_registry}}/{{project_id}}/{{repository}} {{target_registry}}/{{project_id}}/{{repository}}`

- Տպեք պատկերներ, որոնք կարող են հավաքվել աղբից.:

`gcrane gc {{registry}}/{{project_id}}/{{repository}}`

- Ջնջել պատկերները, որոնք կարող են աղբ հավաքվել.:

`gcrane gc {{registry}}/{{project_id}}/{{repository}} | xargs {{[-n|--max-args]}} 1 gcrane delete`

- Նշեք հատուկ գրանցամատյան՝ հատուկ ID-ով.:

`gcrane ls {{gcr.io}}/{{my-project-id}}`

- Տեղափոխեք բոլոր պատկերները ԱՄՆ ռեգիստրից ԵՄ ռեգիստր.:

`gcrane cp {{[-r|--recursive]}} {{gcr.io}}/{{my-project-id}}/{{repository}} {{eu.gcr.io}}/{{my-project-id}}/{{repository}}`
