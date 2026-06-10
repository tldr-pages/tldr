# gcloud կոնֆիգուրացիա

> Կառավարեք `gcloud`-ի տարբեր կազմաձևերը:.
> Տես նաև՝ `gcloud`:.
> Լրացուցիչ տեղեկություններ. <https://docs.cloud.google.com/sdk/gcloud/reference/config>:.

- Սահմանեք հատկություն (ինչպես հաշվարկը/գոտին) ընթացիկ կազմաձևման համար.:

`gcloud config set {{property}} {{value}}`

- Վերցրեք `gcloud` հատկության արժեքը.:

`gcloud config get {{property}}`

- Ցուցադրել բոլոր հատկությունները ընթացիկ կազմաձևման համար.:

`gcloud config list`

- Ստեղծեք նոր կոնֆիգուրացիա տվյալ անունով.:

`gcloud config configurations create {{configuration_name}}`

- Ցուցադրել բոլոր առկա կոնֆիգուրացիաների ցանկը.:

`gcloud config configurations list`

- Անցում տվյալ անունով գոյություն ունեցող կազմաձևին.:

`gcloud config configurations activate {{configuration_name}}`
