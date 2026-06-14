# sv

> Վերահսկել գործող runsv ծառայությունը:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/sv>:.

- Ծառայություն սկսել.:

`sudo sv up {{path/to/service}}`

- Դադարեցնել ծառայությունը.:

`sudo sv down {{path/to/service}}`

- Ստացեք ծառայության կարգավիճակը.:

`sudo sv status {{path/to/service}}`

- Վերբեռնեք ծառայությունը.:

`sudo sv reload {{path/to/service}}`

- Սկսեք ծառայություն, բայց միայն այն դեպքում, եթե այն չի աշխատում և մի վերագործարկեք այն, եթե այն դադարեցվի.:

`sudo sv once {{path/to/service}}`
