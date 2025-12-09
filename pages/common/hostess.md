# hostess

> Manage the `/etc/hosts` file.
> More information: <https://github.com/cbednarski/hostess>.

- List domains, target IP addresses and on/off status:

`hostess list`

- Add a domain pointing to your machine to your hosts file:

`hostess add {{local.example.com}} {{127.0.0.1}}`

- Remove a domain from your hosts file:

`hostess del {{local.example.com}}`

- Disable a domain (but don't remove it):

`hostess off {{local.example.com}}`
