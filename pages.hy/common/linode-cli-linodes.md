# linode-cli linodes

> Կառավարեք Linode-ի դեպքերը:.
> Տես նաև՝ `linode-cli`:.
> Լրացուցիչ տեղեկություններ. <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-compute-instances>:.

- Թվարկեք բոլոր լինոդները.:

`linode-cli linodes list`

- Ստեղծեք նոր Linode.:

`linode-cli linodes create --type {{linode_type}} --region {{region}} --image {{image_id}}`

- Դիտեք կոնկրետ Linode-ի մանրամասները.:

`linode-cli linodes view {{linode_id}}`

- Թարմացրեք պարամետրերը Linode-ի համար.:

`linode-cli linodes update {{linode_id}} --label {{new_label}}`

- Ջնջել Linode:

`linode-cli linodes delete {{linode_id}}`

- Կատարեք էներգիայի կառավարման գործողություն Linode-ի վրա.:

`linode-cli linodes {{boot|reboot|shutdown}} {{linode_id}}`

- Ցուցակեք Linode-ի հասանելի կրկնօրինակները.:

`linode-cli linodes backups-list {{linode_id}}`

- Վերականգնել կրկնօրինակը Linode-ում.:

`linode-cli linodes backups-restore {{linode_id}} --backup-id {{backup_id}}`
