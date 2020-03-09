# Medusa

> A modular and parallel login brute-forcer for a variety of protocols.

- Execute brute force using a list of usernames and passwords:

`medusa -M Method -h target -U {{username_file}} -P {{password_file}}`

- FTP:

`medusa -M ftp -h host -U {{username_file}} -P {{password_file}}`

- HTTP:

`medusa -M HTTP -h host -u username -p password`
