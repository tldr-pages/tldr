# linode-cli տիրույթներ

> Կառավարեք Linode տիրույթները և DNS-ի կոնֆիգուրացիան:.
> Տես նաև՝ `linode-cli`:.
> Լրացուցիչ տեղեկություններ. <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-the-dns-manager>:.

- Նշեք բոլոր կառավարվող տիրույթները.:

`linode-cli domains list`

- Ստեղծեք նոր կառավարվող տիրույթ.:

`linode-cli domains create --domain {{domain_name}} --type {{master|slave}} --soa-email {{email}}`

- Դիտեք կոնկրետ տիրույթի մանրամասները.:

`linode-cli domains view {{domain_id}}`

- Ջնջել կառավարվող տիրույթը.:

`linode-cli domains delete {{domain_id}}`

- Նշեք գրառումները որոշակի տիրույթի համար.:

`linode-cli domains records-list {{domain_id}}`

- Ավելացնել DNS գրառում տիրույթում.:

`linode-cli domains records-create {{domain_id}} --type {{A|AAAA|CNAME|MX|...}} --name {{subdomain}} --target {{target_value}}`

- Թարմացրեք DNS գրառումը տիրույթի համար.:

`linode-cli domains records-update {{domain_id}} {{record_id}} --target {{new_target_value}}`

- Ջնջել DNS գրառումը տիրույթից.:

`linode-cli domains records-delete {{domain_id}} {{record_id}}`
