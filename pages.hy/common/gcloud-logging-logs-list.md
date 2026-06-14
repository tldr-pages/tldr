# gcloud logging logs ցուցակ

> Ցուցակագրեք տեղեկամատյանները Google Cloud նախագծում:.
> Օգտակար է մոնիտորինգի և վերլուծության համար հասանելի տեղեկամատյանները հայտնաբերելու համար:.
> Տես նաև՝ `gcloud`:.
> Լրացուցիչ տեղեկություններ. <https://docs.cloud.google.com/sdk/gcloud/reference/logging/logs/list>:.

- Թվարկեք ընթացիկ նախագծի բոլոր տեղեկամատյանները.:

`gcloud logging logs list`

- Թվարկեք բոլոր տեղեկամատյանները հատուկ մատյան դույլի և գտնվելու վայրի համար.:

`gcloud logging logs list --bucket={{bucket_id}} --location={{location}}`

- Ցուցակեք բոլոր տեղեկամատյանները հատուկ դիտման համար մատյան դույլով.:

`gcloud logging logs list --bucket={{bucket_id}} --location={{location}} --view={{view_id}}`

- Ցուցակագրեք տեղեկամատյանները ֆիլտրի արտահայտությամբ.:

`gcloud logging logs list --filter="{{expression}}"`

- Նշեք տեղեկամատյանների նշված քանակությունը.:

`gcloud logging logs list --limit={{number}}`

- Ցուցակագրեք տեղեկամատյանները՝ տեսակավորված ըստ որոշակի դաշտի՝ աճման կամ նվազման կարգով (`~` նվազման համար).:

`gcloud logging logs list --sort-by="{{field_name}}"`

- Ցուցակ տեղեկամատյանները՝ դասավորված ըստ բազմաթիվ դաշտերի.:

`gcloud logging logs list --sort-by="{{field1}},~{{field2}}"`

- Ցուցակեք տեղեկամատյանները՝ մանրամասն ելքով՝ ցույց տալով լրացուցիչ մանրամասներ.:

`gcloud logging logs list --verbosity=debug`
