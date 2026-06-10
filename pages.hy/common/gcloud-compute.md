# gcloud հաշվարկ

> Ստեղծեք, գործարկեք և կառավարեք VM-ներ Google Cloud ենթակառուցվածքում:.
> Տես նաև՝ `gcloud`:.
> Լրացուցիչ տեղեկություններ. <https://docs.cloud.google.com/sdk/gcloud/reference/compute>:.

- Թվարկեք Հաշվողական շարժիչի գոտիները.:

`gcloud compute zones list`

- Ստեղծեք VM օրինակ.:

`gcloud compute instances create {{instance_name}}`

- Ցուցադրել VM օրինակի մանրամասները.:

`gcloud compute instances describe {{instance_name}}`

- Թվարկեք բոլոր VM օրինակները նախագծում.:

`gcloud compute instances list`

- Ստեղծեք մշտական սկավառակի լուսանկար.:

`gcloud compute disks snapshot {{disk_name}} --snapshot-names {{snapshot_name}}`

- Ցուցադրել նկարի մանրամասները.:

`gcloud compute snapshots describe {{snapshot_name}}`

- Ջնջել նկարը.:

`gcloud compute snapshots delete {{snapshot_name}}`

- Միացեք VM օրինակին, օգտագործելով SSH:

`gcloud compute ssh {{instance_name}}`
