# ldapdomaindump

> Dump users, computers, groups, OS and membership information via LDAP to HTML, JSON and greppable output.
> See also `ldapsearch`.
> More information: <https://github.com/dirkjanm/ldapdomaindump#usage>.

- Dump all information using the given LDAP account:

`ldapdomaindump {{[-u|--user]}} {{domain}}\{{username}} {{[-p|--password]}} {{password|ntlm_hash}} {{hostname|ip}}`

- Dump all information, resolving computer hostnames:

`ldapdomaindump {{[-r|--resolve]}} {{[-u|--user]}} {{domain}}\{{username}} {{[-p|--password]}}{{password}} {{hostname|ip}}`

- Dump all information, resolving computer hostnames with the selected DNS server:

`ldapdomaindump {{[-r|--resolve]}} {{[-n|--dns-server]}} {{domain_controller_ip}} {{[-u|--user]}} {{domain}}\{{username}} {{[-p|--password]}}{{password}} {{hostname|ip}}`

- Dump all information to the given directory without JSON output:

`ldapdomaindump --no-json {{[-o|--outdir]}} {{path/to/directory}} {{[-u|--user]}} {{domain}}\{{username}} {{[-p|--password]}}{{password}} {{hostname|ip}}`
