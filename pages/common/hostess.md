# hostess

> An idempotent command-line utility for managing your /etc/hosts file.
> More information: <https://github.com/cbednarski/hostess>.

- List domains, target ips and on/off status:

`hostess list`

- Add a domain pointing to your machine to your hosts file:

`hostess add {{local.example.com}} {{127.0.0.1}}`

- Remove a domain from your hosts file:

`hostess del {{local.example.com}}`

- Disable a domain (but don't remove it completely):

`hostess off {{local.example.com}}`
