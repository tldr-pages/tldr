# Medusa

> Un brute-forcer de conectare modular și paralel pentru o varietate de protocoale.

- Execută forță brută împotriva unui server FTP folosind un fișier care conține nume de utilizator și un fișier care conține parole:

`medusa -M ftp -h host -U {{path/to/username_file}} -P {{path/to/password_file}}`

- Executa o incercare de autentificare impotriva unui server HTTP folosind numele de utilizator, parola si agentul de utilizator specificat:

`medusa -M HTTP -h host -u {{username}} -p {{password}} -m USER-AGENT:"{{Agent}}"`

- Execută o forță brută împotriva unui server MySQL folosind un fișier care conține nume de utilizator și un hash:

`medusa -M mysql -h host -U {{path/to/username_file}} -p {{hash}} -m PASS:HASH`

- Execută o forță brută împotriva unei liste de servere SMB folosind un nume de utilizator și un fișier pwdump:

`medusa -M smbnt -H {{path/to/hosts_file}} -C {{path/to/pwdump_file}} -u {{username}} -m PASS:HASH`
