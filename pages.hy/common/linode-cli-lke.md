# linode-cli lke

> Կառավարեք Linode Kubernetes Engine (LKE) կլաստերները:.
> Տես նաև՝ `linode-cli`:.
> Լրացուցիչ տեղեկություններ. <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-lke>:.

- Թվարկեք բոլոր LKE կլաստերները.:

`linode-cli lke clusters list`

- Ստեղծեք նոր LKE կլաստեր.:

`linode-cli lke clusters create --region {{region}} --type {{type}} --node-type {{node_type}} --nodes-count {{count}}`

- Դիտեք կոնկրետ LKE կլաստերի մանրամասները.:

`linode-cli lke clusters view {{cluster_id}}`

- Թարմացրեք գոյություն ունեցող LKE կլաստերը.:

`linode-cli lke clusters update {{cluster_id}} --node-type {{new_node_type}}`

- Ջնջել LKE կլաստերը՝:

`linode-cli lke clusters delete {{cluster_id}}`
