# ibmcloud ես

> Կառավարեք ինքնությունը և ռեսուրսների հասանելիությունը:.
> Լրացուցիչ տեղեկություններ. <https://cloud.ibm.com/docs/cli?topic=cli-ibmcloud_commands_iam>:.

- Նշեք ծառայության ID-ները հաշվում.:

`ibmcloud iam service-ids`

- Թվարկեք բոլոր API ստեղները ծառայության ID-ի համար.:

`ibmcloud iam service-api-keys {{service_id}}`

- Ստեղծեք API բանալի ծառայության ID-ի համար՝ նկարագրությամբ և առանց հաստատման.:

`ibmcloud iam service-api-key-create {{api_key_name}} {{service_id}} {{[-d|--description]}} {{description}} {{[-f|--force]}}`

- Թվարկեք այս հրամանի ներքո հասանելի բոլոր գործողությունները.:

`ibmcloud iam help`
