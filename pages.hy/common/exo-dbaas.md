# exo dbaas

> Կառավարեք Exoscale DBaaS-ը:.
> Լրացուցիչ տեղեկություններ. <https://community.exoscale.com/product/dbaas/>:.

- Ցուցակեք տվյալների բազայի ծառայության տեսակները.:

`exo dbaas type list`

- Ցուցակեք առկա ծրագրերը տվյալների բազայի ծառայության տեսակի համար.:

`exo dbaas type show {{database_service_type}} --plans`

- Ստեղծեք տվյալների բազայի նոր ծառայություն (ծառայություն մուտք գործելու համար պետք է նշվի IP ֆիլտր).:

`exo dbaas create {{database_service_type}} {{database_service_type_plan}} {{database_service_name}} --{{database_service_type}}-ip-filter {{1.2.3.4/32}}`

- Ցույց տալ կապի URI-ն տվյալների բազայի ծառայության համար.:

`exo dbaas show {{database_service_name}} --uri`

- Տվյալների շտեմարանի ծառայության համար սահմանեք սպասարկման սահմանված ժամանակը և շաբաթվա օրը.:

`exo dbaas update {{database_service_name}} --maintenance-dow {{day_of_the_week}} --maintenance-time {{HH:MM:SS}}`

- Ստացեք օգնություն տվյալների բազայի ծառայության հատուկ տեսակի համար.:

`exo dbaas {{subcommand}} --help-{{database_service_type}}`
