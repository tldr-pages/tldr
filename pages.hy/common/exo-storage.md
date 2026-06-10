# exo պահեստավորում

> Կառավարեք Exoscale Simple Object Storage (SOS) ծառայությունը:.
> Լրացուցիչ տեղեկություններ. <https://community.exoscale.com/product/storage/object-storage/>:.

- Ստեղծեք նոր SOS դույլ.:

`exo storage mb {{bucket_name}}`

- Վերբեռնեք ֆայլը դույլի մեջ.:

`exo storage put {{path/to/file}} {{bucket_name}}/{{prefix/}}`

- Թվարկե՛ք առարկաները դույլի մեջ.:

`exo storage ls {{bucket_name}}`

- Մոդելավորել օբյեկտի ներբեռնումը դույլից.:

`exo storage get {{bucket_name}}/{{object_key}} {{local_path}} --dry-run`

- Կառավարեք օբյեկտի մետատվյալները.:

`exo storage metadata add {{bucket_name}}/{{object_key}} {{key=value}}`
