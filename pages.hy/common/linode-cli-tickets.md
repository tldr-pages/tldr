# linode-cli տոմսեր

> Կառավարեք Linode-ի աջակցության տոմսերը:.
> Տես նաև՝ `linode-cli`:.
> Լրացուցիչ տեղեկություններ. <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-account-management>:.

- Նշեք ձեր աջակցության տոմսերը.:

`linode-cli tickets list`

- Բացեք նոր տոմս.:

`linode-cli tickets create --summary "{{Summary or quick title for the Ticket}}" --description "{{Detailed description of the issue}}"`

- Ցուցակեք տոմսի պատասխանները.:

`linode-cli tickets replies {{ticket_id}}`

- Պատասխանել կոնկրետ տոմսին.:

`linode-cli tickets reply {{ticket_id}} --description "{{The content of your reply}}"`
