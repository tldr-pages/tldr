# elasticsորոն-օգտատերեր

> Կառավարեք Elasticsearch-ում բնիկ ոլորտի օգտատերերին, ներառյալ օգտատերերի ստեղծումը, թարմացումը և ջնջումը:.
> Լրացուցիչ տեղեկություններ. <https://www.elastic.co/docs/reference/elasticsearch/command-line-tools/users-command>:.

- Ինտերակտիվ կերպով ավելացրեք նոր օգտվող (գաղտնաբառի հուշում).:

`elasticsearch-users useradd {{username}}`

- Ավելացրեք նոր օգտվող և նշեք դերերը.:

`elasticsearch-users useradd {{username}} -r {{role1,role2}}`

- Փոխեք գաղտնաբառը գոյություն ունեցող օգտվողի համար.:

`elasticsearch-users passwd {{username}}`

- Ջնջել օգտվողին.:

`elasticsearch-users userdel {{username}}`

- Թվարկեք բոլոր օգտվողներին հայրենի ոլորտում.:

`elasticsearch-users list`
