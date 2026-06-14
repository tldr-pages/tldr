# htpasswd

> Ստեղծեք և կառավարեք htpasswd ֆայլեր՝ վեբ սերվերի դիրեկտորիաները պաշտպանելու համար՝ օգտագործելով հիմնական նույնականացումը:.
> Լրացուցիչ տեղեկություններ. <https://httpd.apache.org/docs/current/programs/htpasswd.html>:.

- Ստեղծեք/վերագրեք htpasswd ֆայլ.:

`htpasswd -c {{path/to/file}} {{username}}`

- Ավելացրեք օգտվողին htpasswd ֆայլում կամ թարմացրեք առկա օգտվողին.:

`htpasswd {{path/to/file}} {{username}}`

- Ավելացրեք օգտվողին htpasswd ֆայլին խմբաքանակի ռեժիմով առանց ինտերակտիվ գաղտնաբառի հուշման (սկրիպտի օգտագործման համար).:

`htpasswd -b {{path/to/file}} {{username}} {{password}}`

- Ջնջել օգտվողին htpasswd ֆայլից.:

`htpasswd -D {{path/to/file}} {{username}}`

- Ստուգեք օգտվողի գաղտնաբառը.:

`htpasswd -v {{path/to/file}} {{username}}`

- Ցուցադրել տող օգտանունով (պարզ տեքստ) և գաղտնաբառով (md5):

`htpasswd -nbm {{username}} {{password}}`
