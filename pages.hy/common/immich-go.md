#իմմիչ-գնա

> Immich-Go-ն բաց կոդով գործիք է, որը նախատեսված է մեծ լուսանկարների հավաքածուների վերբեռնումը ձեր ինքնակառավարվող Immich սերվերում հեշտացնելու համար:.
> Տես նաև՝ `immich`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/simulot/immich-go>:.

- Վերբեռնեք Google Photos-ի ֆայլը Immich սերվերում՝:

`immich-go -server={{server_url}} -key={{server_key}} upload {{path/to/takeout_file.zip}}`

- Ներմուծեք 2019 թվականի հունիսին նկարահանված լուսանկարները՝ ալբոմների ավտոմատ ստեղծման ժամանակ.:

`immich-go -server={{server_url}} -key={{server_key}} upload -create-albums -google-photos -date={{2019-06}} {{path/to/takeout_file.zip}}`

- Վերբեռնեք ֆայլ՝ օգտագործելով սերվերը և բանալիը կազմաձևման ֆայլից.:

`immich-go -use-configuration={{~/.immich-go/immich-go.json}} upload {{path/to/takeout_file.zip}}`

- Ուսումնասիրեք Immich սերվերի բովանդակությունը, հեռացրեք ավելի քիչ որակի պատկերներ և պահպանեք ալբոմները.:

`immich-go -server={{server_url}} -key={{server_key}} duplicate -yes`

- Ջնջել բոլոր ալբոմները, որոնք ստեղծված են «YYYY-MM-DD» օրինակով.:

`immich-go -server={{server_url}} -key={{server_key}} tool album delete {{\d{4}-\d{2}-\d{2}}}`
