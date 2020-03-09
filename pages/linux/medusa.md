# Medusa

> A speedy, parallel, and modular, login brute-forcer.
> More information: <https://manpages.debian.org/buster/apache2/a2disconf.8.en.html>.

- General:
`medusa -M Method -h target -U {{username_file}} -P {{password_file}}`

- FTP:
`medusa -M ftp -h host -U {{username_file}} -P {{password_file}}`

- HTTP:
`medusa -M HTTP -h host -u username -p password`
