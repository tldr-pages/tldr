# gcloud բաղադրիչ

> Կառավարեք Google Cloud CLI բաղադրիչները:.
> Տես նաև՝ `gcloud`:.
> Լրացուցիչ տեղեկություններ. <https://docs.cloud.google.com/sdk/gcloud/reference/components>:.

- Դիտեք տեղադրման համար հասանելի բաղադրիչները.:

`gcloud components list`

- Տեղադրեք մեկ կամ մի քանի բաղադրիչ (տեղադրում է նաև ցանկացած կախվածություն).:

`gcloud components install {{component_id1 component_id2 ...}}`

- Թարմացրեք բոլոր բաղադրիչները վերջին տարբերակին.:

`gcloud components update`

- Թարմացրեք բոլոր բաղադրիչները որոշակի տարբերակի.:

`gcloud components update --version={{1.2.3}}`

- Թարմացրեք բաղադրիչները առանց հաստատման (օգտակար ավտոմատացման սցենարների համար).:

`gcloud components update --quiet`
