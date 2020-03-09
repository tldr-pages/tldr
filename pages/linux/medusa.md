# Medusa

> A modular and parallel login brute-forcer for a variety of protocols.

- Execute brute force against a ftp server using a file containing usernames and a file containing passwords:

`medusa -M ftp -h host -U {{username_file}} -P {{password_file}}`

- Execute a login attempt against a HTTP server using the username, password and user-agent specified:

`medusa -M HTTP -h host -u {{username}} -p {{password}} -m USER-AGENT:"{{Agent}}"`

- Execute a brute force against a MySQL server using a file cointaining usernames and a hash:

`medusa -M mysql -h host -U {{username_file}} -p {{hash}} -m PASS:HASH`

- Execute a brute force against a list of SMB server using a username and a pwdump file:

`medusa -M smbnt -H {{hosts_file}} -C {{pwdump_file}} -u {{user}} -m PASS:HASH`
