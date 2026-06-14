# linode-cli հատորներ

> Կառավարեք Linode ծավալները:.
> Տես նաև՝ `linode-cli`:.
> Լրացուցիչ տեղեկություններ. <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-block-storage-volumes>:.

- Ցուցակեք ընթացիկ ծավալները.:

`linode-cli volumes list`

- Ստեղծեք նոր հատոր և կցեք այն կոնկրետ Linode-ին.:

`linode-cli volumes create --label {{volume_label}} --size {{size_in_GB}} --linode-id {{linode_id}}`

- Կցեք ծավալը կոնկրետ Linode-ին.:

`linode-cli volumes attach {{volume_id}} --linode-id {{linode_id}}`

- Անջատեք հատորը լինոդից.:

`linode-cli volumes detach {{volume_id}}`

- Չափափոխել ծավալը (Նշում. Չափը կարելի է միայն ավելացնել):

`linode-cli volumes resize {{volume_id}} --size {{new_size_in_GB}}`

- Ջնջել ծավալը.:

`linode-cli volumes delete {{volume_id}}`
