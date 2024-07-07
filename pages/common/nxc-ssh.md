# nxc ssh

> Pentest and exploit SSH servers.
> See also: `hydra`.
> More information: <https://www.netexec.wiki/ssh-protocol>.

- Spray the specified [p]assword against a list of [u]sernames on the specified target:

`nxc ssh {{192.168.178.2}} -u {{path/to/usernames.txt}} -p {{password}}`

- Search for valid credentials by trying out every combination in the specified lists of [u]sernames and [p]asswords:

`nxc ssh {{192.168.178.2}} -u {{path/to/usernames.txt}} -p {{path/to/passwords.txt}}`

- Use the specified private key for authentication, using the supplied [p]assword as the key's passphrase:

`nxc ssh {{192.186.178.2}} -u {{path/to/usernames.txt}} -p {{password}} --key-file {{path/to/id_rsa}}`

- Try a combination of [u]sername and [p]assword on a number of targets:

`nxc ssh {{192.168.178.0/24}} -u {{username}} -p {{password}}`

- Check for `sudo` privileges on a successful login:

`nxc ssh {{192.168.178.2}} -u {{username}} -p {{path/to/passwords.txt}} --sudo-check`
