# elasticsearch-reset-password

> Վերականգնել օգտատերերի գաղտնաբառերը հայրենի ոլորտում և ներկառուցված օգտատերերի համար:.
> Լրացուցիչ տեղեկություններ. <https://www.elastic.co/docs/reference/elasticsearch/command-line-tools/reset-password>:.

- Վերականգնել օգտվողի գաղտնաբառը ավտոմատ ստեղծվող արժեքի վրա և տպել այն վահանակում.:

`elasticsearch-reset-password {{[-u|--username]}} {{user}}`

- Ինտերակտիվ կերպով հուշեք վերականգնել գաղտնաբառը հայրենի օգտագործողի համար.:

`elasticsearch-reset-password {{[-u|--username]}} {{user}} {{[-i|--interactive]}}`

- Ինտերակտիվ կերպով վերականգնեք օգտվողի գաղտնաբառը նշված Elasticsearch հանգույցի URL-ում.:

`elasticsearch-reset-password --url {{host}}:{{port}} {{[-u|--username]}} {{user}} {{[-i|--interactive]}}`
