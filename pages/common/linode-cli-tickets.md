# linode-cli tickets

> Manage Linode Support Tickets.
> See also: `linode-cli`.
> More information: <https://www.linode.com/docs/products/tools/cli/guides/account/>.

- List your Support Tickets:

`linode-cli tickets list`

- Open a new Ticket:

`linode-cli tickets create --summary "{{Summary or quick title for the Ticket}}" --description "{{Detailed description of the issue}}"`

- List replies to a Ticket:

`linode-cli tickets replies {{ticket_id}}`

- Reply to a specific Ticket:

`linode-cli tickets reply {{ticket_id}} --description "{{The content of your reply}}"`
