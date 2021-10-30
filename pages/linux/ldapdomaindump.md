# ldapdomaindump

> Dump users, computers, groups, OS and membership information via LDAP to HTML, JSON and greppable output.
> See also `ldapsearch`.
> More information: <https://github.com/dirkjanm/ldapdomaindump>.

- Dump all information using the given LDAP account:

`ldapdomaindump --user {{domain}}\\{{administrator}} --password {{password|ntlm_hash}} {{hostname|ip}}`

- Dump all information, resolving computer hostnames:

`ldapdomaindump --resolve --user {{domain}}\\{{administrator}} --password {{password}} {{hostname|ip}}`

- Dump all information, resolving computer hostnames with the selected DNS server:

`ldapdomaindump --resolve --dns-server {{domain_controller_ip}} --user {{domain}}\\{{administrator}} --password {{password}} {{hostname|ip}}`

- Dump all information to the given directory without JSON output:

`ldapdomaindump --no-json --outdir {{path/to/directory}} --user {{domain}}\\{{administrator}} --password {{password}} {{hostname|ip}}`
