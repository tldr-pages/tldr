# gcloud նախագիծ

> Կառավարեք նախագծի մուտքի քաղաքականությունը Google Cloud-ում:.
> Տես նաև՝ `gcloud`:.
> Լրացուցիչ տեղեկություններ. <https://docs.cloud.google.com/sdk/gcloud/reference/projects>:.

- Ստեղծեք նոր նախագիծ.:

`gcloud projects create {{project_id|project_number}}`

- Թվարկեք բոլոր ակտիվ նախագծերը.:

`gcloud projects list`

- Ցուցադրել մետատվյալները նախագծի համար.:

`gcloud projects describe {{project_id}}`

- Ջնջել նախագիծը.:

`gcloud projects delete {{project_id|project_number}}`

- Ավելացրեք IAM քաղաքականություն, որը պարտադիր է նշված նախագծին.:

`gcloud projects add-iam-policy-binding {{project_id}} --member {{principal}} --role {{role}}`
