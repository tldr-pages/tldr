# Medusa

> A modular and parallel login brute-forcer for a variety of protocols.
> More information: <https://jmk-foofus.github.io/medusa/medusa.html>.

- Execute brute force against an FTP server using a file containing usernames and a file containing passwords:

`medusa -M ftp -h host -U {{path/to/username_file}} -P {{path/to/password_file}}`

- Execute a login attempt against an HTTP server using the username, password and user-agent specified:

`medusa -M HTTP -h host -u {{username}} -p {{password}} -m USER-AGENT:"{{Agent}}"`

- Execute a brute force against a MySQL server using a file containing usernames and a hash:

`medusa -M mysql -h host -U {{path/to/username_file}} -p {{hash}} -m PASS:HASH`

- Execute a brute force against a list of SMB servers using a username and a pwdump file:

`medusa -M smbnt -H {{path/to/hosts_file}} -C {{path/to/pwdump_file}} -u {{username}} -m PASS:HASH`
