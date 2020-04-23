# hydra

> Online password guessing tool.
> Protocols supported include FTP, HTTP(S), SMTP, SNMP, XMPP, SSH, and more.
> More information: <https://github.com/vanhauser-thc/thc-hydra>.

- Start Hydra's wizard:

`hydra-wizard`

- Guess SSH credentials using a given username and a list of passwords:

`hydra -l {{username}} -P {{path/to/wordlist.txt}} {{host_ip}} {{ssh}}`

- Guess Telnet credentials using a list of usernames and a single password, specifying a non-standard port and IPv6:

`hydra -L {{path/to/usernames.txt}} -p {{password}} -s {{port}} -6 {{host_ip}} {{telnet}}`

- Guess FTP credentials using usernames and passwords lists, specifying the number of threads:

`hydra -L {{path/to/usernames.txt}} -P {{path/to/wordlist.txt}} -t {{n_tasks}} {{host_ip}} {{ftp}}`

- Guess MySQL credentials using a username and a passwords list, exiting when a username/password pair is found:

`hydra -l {{username}} -P {{path/to/wordlist.txt}} -f {{host_ip}} {{mysql}}`

- Guess RDP credentials using a username and a passwords list, showing each attempt:

`hydra -l {{username}} -P {{path/to/wordlist.txt}} -V {{rdp://host_ip}}`

- Guess IMAP credentials on a range of hosts using a list of colon-separated username/password pairs:

`hydra -C {{path/to/username_password_pairs.txt}} {{imap://[host_range_cidr]}}`

- Guess POP3 credentials on a list of hosts using usernames and passwords lists, exiting when a username/password pair is found:

`hydra -L {{path/to/usernames.txt}} -P {{path/to/wordlist.txt}} -M {{path/to/hosts.txt}} -F {{pop3}}`
