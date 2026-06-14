# croc

> Ուղարկեք և ստացեք ֆայլեր հեշտությամբ և ապահով ցանկացած ցանցի միջոցով:.
> Լրացուցիչ տեղեկություններ. <https://github.com/schollz/croc>:.

- Ուղարկեք ֆայլ կամ գրացուցակ.:

`croc send {{path/to/file_or_directory}}`

- Ուղարկեք ֆայլ կամ գրացուցակ հատուկ անցաբառով.:

`croc send {{[-c|--code]}} {{passphrase}} {{path/to/file_or_directory}}`

- Ստացեք ֆայլ կամ գրացուցակ ստացող մեքենայի վրա.:

`croc {{passphrase}}`

- Ուղարկեք և միացեք մաքսային ռելեի միջոցով.:

`croc --relay {{ip_to_relay}} send {{path/to/file_or_directory}}`

- Ստացեք և միացեք մաքսային ռելեի միջոցով.:

`croc --relay {{ip_to_relay}} {{passphrase}}`

- Տեղադրեք croc ռելե լռելյայն նավահանգիստների վրա.:

`croc relay`

- Ցուցադրել croc հրամանի պարամետրերը և տարբերակները.:

`croc {{send|relay}} --help`
