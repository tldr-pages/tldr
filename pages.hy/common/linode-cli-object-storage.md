# linode-cli օբյեկտ-պահեստավորում

> Կառավարեք Linode օբյեկտների պահեստը:.
> Տես նաև՝ `linode-cli`:.
> Լրացուցիչ տեղեկություններ. <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-object-storage>:.

- Նշեք օբյեկտների պահպանման բոլոր դույլերը.:

`linode-cli object-storage buckets list`

- Ստեղծեք նոր օբյեկտների պահեստավորման դույլ.:

`linode-cli object-storage buckets create --cluster {{cluster_id}} --label {{bucket_label}}`

- Ջնջել օբյեկտների պահպանման դույլը.:

`linode-cli object-storage buckets delete {{cluster_id}} {{bucket_label}}`

- Ցուցակեք Օբյեկտների պահպանման կլաստերի շրջանները.:

`linode-cli object-storage clusters list`

- Ցուցակ մուտքի ստեղներ օբյեկտների պահպանման համար.:

`linode-cli object-storage keys list`

- Ստեղծեք նոր մուտքի բանալի Object Storage-ի համար.:

`linode-cli object-storage keys create --label {{label}}`

- Օբյեկտների պահպանման համար չեղյալ համարել մուտքի բանալին.:

`linode-cli object-storage keys revoke {{access_key_id}}`
