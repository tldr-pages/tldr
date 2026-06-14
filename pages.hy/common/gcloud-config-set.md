# gcloud կազմաձևման հավաքածու

> Սահմանեք հատկություն Google Cloud CLI-ի կազմաձևում:.
> Հատկությունները վերահսկում են Google Cloud CLI-ի վարքագծի տարբեր ասպեկտները:.
> Լրացուցիչ տեղեկություններ. <https://docs.cloud.google.com/sdk/gcloud/reference/config/set>:.

- Սահմանեք նախագծի հատկությունը հիմնական բաժնում.:

`gcloud config set project {{project_id}}`

- Սահմանեք հաշվարկային գոտին ապագա գործողությունների համար.:

`gcloud config set compute/zone {{zone_name}}`

- Անջատել հուշումը, որպեսզի gcloud-ը հարմար լինի սկրիպտավորման համար.:

`gcloud config set disable_prompts true`

- Դիտեք ներկայումս օգտագործվող հատկությունների ցանկը.:

`gcloud config list`

- Չեղարկել նախկինում սահմանված հատկությունը.:

`gcloud config unset {{property_name}}`

- Ստեղծեք նոր կազմաձևման պրոֆիլ.:

`gcloud config configurations create {{configuration_name}}`

- Անցում տարբեր կազմաձևման պրոֆիլների միջև.:

`gcloud config configurations activate {{configuration_name}}`
